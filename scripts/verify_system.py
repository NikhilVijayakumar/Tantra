import sys
import logging
from pathlib import Path
import yaml
import shutil
import json
import datetime

# Add src to path to ensure we use the local package
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

NIBANDHA_INSTALLED = False
try:
    from nibandha import Nibandha
    from nibandha.configuration.infrastructure.file_loader import FileConfigLoader
    from nibandha.configuration.domain.models.app_config import AppConfig
    from nibandha.configuration.domain.models.reporting_config import ReportingConfig
    from nibandha.reporting import ReportGenerator
    from nibandha.reporting.shared.data.data_builders import SummaryDataBuilder
    from nibandha.reporting.shared.domain.protocols.module_discovery import ModuleDiscoveryProtocol
    NIBANDHA_INSTALLED = True
    
    # Attempt rebuild pydantic models if needed
    try:
        ReportingConfig.model_rebuild()
    except Exception as e:
        print(f"Warning: Could not rebuild ReportingConfig: {e}")
        
except ImportError as e:
    print(f"DEBUG: Import Error: {e}")
    NIBANDHA_INSTALLED = False

class TantraCoreDiscovery:
    """
    Explicitly defines TANTRA's 8 Core Modules for reporting.
    Implements ModuleDiscoveryProtocol.
    """
    def discover_modules(self, source_root: Path) -> list[str]:
        return [
            "Semantic",
            "Entity",
            "Structure",
            "Topic",
            "Grammar",
            "Relation",
            "Density",
            "Anomaly"
        ]

def run_basic_verification():
    """Fallback when Nibandha is not installed."""
    print("\n[⚠️] Nibandha Infrastructure NOT found. Running Basic Verification (Pytest only).")
    import subprocess
    
    output_dir = Path(".agent_reports/assets/data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    unit_json = output_dir / "unit.json"
    
    # Run Valid Unit Tests
    cmd = [sys.executable, "-m", "pytest", "tests/unit", f"--json-report-file={unit_json}", "--json-report"]
    print(f"    Running: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=False) 
        if unit_json.exists():
            print(f"    ✅ Unit Test Report generated: {unit_json}")
            with open(unit_json) as f:
                data = json.load(f)
                summary = data.get("summary", {})
                passed = summary.get("passed", 0)
                failed = summary.get("failed", 0)
                print(f"       Passed: {passed}, Failed: {failed}")
        else:
            print("    ❌ Failed to generate JSON report. Install pytest-json-report.")
            
    except Exception as e:
        print(f"    ❌ Execution failed: {e}")

def main():
    print(">>> TANTRA System Verification <<<")
    
    if not NIBANDHA_INSTALLED:
        run_basic_verification()
        return

    # 2. Initialize System
    print(f"\n[1] Initializing TANTRA Verification (Using Nibandha)")
    
    # We create a dummy AppConfig for verification context
    try:
        app_config = AppConfig(
            name="TANTRA-Verification",
            environment="DEV",
            log_level="INFO",
            version="1.0.0",
            custom_folders=["logs", "reports"]
        )
        
        app = Nibandha(app_config, root_name=".Tantra")
        app.bind()
        print(f"    ✅ Bound to: {app.app_root}")
        
    except Exception as e:
        print(f"❌ Failed to initialize app: {e}")
        sys.exit(1)

    # 3. Verify Reporting
    print(f"\n[2] Generating Quality Reports")
    try:
        # Output directory for reports
        report_dir = app.app_root / "Report"
        
        # Configure the Nibandha Report Generator to analyze *TANTRA*
        # Source root is 'src/bavans/tantra'
        config = ReportingConfig(
            output_dir=str(report_dir),
            docs_dir=str(project_root / "docs"),
            export_formats=["md", "html"],
            project_name="TANTRA",
            quality_target="src/bavans/tantra", 
            package_roots=["bavans", "tantra"],
            module_discovery=TantraCoreDiscovery() # Explicit Discovery
        )
        
        generator = ReportGenerator(config=config)
        print(f"    Generator Output Dir: {generator.output_dir}")
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 1. Introduction
        generator.intro_reporter.generate()
        print(f"    ✅ Introduction generated")

        # 2. Unit Tests
        print(f"    Running Unit Tests (tests/unit)...")
        unit_data = generator.run_unit_Tests("tests/unit", timestamp)
        
        # 3. E2E Tests (Fallback to Integration if E2E missing)
        e2e_data = {} 
        e2e_target = None
        
        if (project_root / "tests/e2e").exists():
            e2e_target = "tests/e2e"
        elif (project_root / "tests/integration").exists():
            print(f"    ⚠️ 'tests/e2e' not found. Using 'tests/integration' as E2E target.")
            e2e_target = "tests/integration"
            
        if e2e_target:
             e2e_data = generator.run_e2e_Tests(e2e_target, timestamp)
        else:
             print(f"    ⚠️ No E2E or Integration tests found. Skipping E2E report.")

        # 4. Code Quality (Cyclomatic, Maintainability)
        print(f"    Running Quality Analysis...")
        quality_data = generator.run_quality_checks("src/bavans/tantra")
        
        # 5. Dependency Analysis
        print(f"    Running Dependency Analysis...")
        actual_src_root = project_root / "src/bavans/tantra"
        dep_data = generator.run_dependency_checks(
            actual_src_root,
            package_roots=["bavans.tantra"]
        )
        
        # 6. Package Metadata
        print(f"    Running Package Checks...")
        pkg_data = generator.run_package_checks(project_root)

        # 7. Documentation
        print(f"    Running Documentation Audit...")
        doc_data = generator.doc_reporter.generate(project_root)

        # 8. Save Artifacts (JSON) for Agents
        assets_dir = generator.output_dir / "assets" / "data"
        assets_dir.mkdir(parents=True, exist_ok=True)
        
        for name, data in [("quality", quality_data), ("dependency", dep_data), ("package", pkg_data), ("documentation", doc_data)]:
             if data:
                 with open(assets_dir / f"{name}.json", 'w') as f:
                     json.dump(data, f, indent=2, default=str)
                 print(f"    ✅ {name.capitalize()} Artifact saved")

        # 9. Conclusion
        summary_builder = SummaryDataBuilder()
        summary_data = summary_builder.build(unit_data, e2e_data, quality_data, documentation_data=doc_data, dependency_data=dep_data, package_data=pkg_data)
        
        generator.template_engine.render(
            "conclusion_template.md",
            summary_data,
            generator.output_dir / "details" / "11_conclusion.md"
        )
        print(f"    ✅ Conclusion Report generated")
        
        # 10. Global References & Export
        generator._generate_global_references(timestamp)
        generator._export_reports()
        print(f"    ✅ Exports triggered: {report_dir}")
        print(f"    ✅ View Report: {report_dir / 'unified_report.html'}")

    except Exception as e:
        print(f"    ❌ Reporting check failed: {e}")
        import traceback
        traceback.print_exc()

    print("\n>>> Verification Complete <<<")

if __name__ == "__main__":
    main()
