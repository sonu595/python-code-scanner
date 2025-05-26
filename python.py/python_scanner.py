import subprocess

def run_bandit(target_path):
    print("\n[+] Running Bandit Security Scan...")
    result = subprocess.run(["bandit", "-r", target_path, "-f", "json", "-o", "bandit_report.json"], capture_output=True, text=True)
    if result.returncode == 0:
        print("[+] Bandit scan completed successfully. Report saved as bandit_report.json")
    else:
        print("[-] Bandit scan failed!")
        print(result.stderr)

def run_semgrep(target_path):
    print("\n[+] Running Semgrep Security Scan...")
    result = subprocess.run(["semgrep", "--config=auto", target_path, "--json", "--output", "semgrep_report.json"], capture_output=True, text=True)
    if result.returncode == 0:
        print("[+] Semgrep scan completed successfully. Report saved as semgrep_report.json")
    else:
        print("[-] Semgrep scan failed!")
        print(result.stderr)

def main():
    target_path = input("Enter the path to your Python project folder: ").strip()

    if not target_path:
        print("[-] No path provided. Exiting.")
        return

    run_bandit(target_path)
    run_semgrep(target_path)

    print("\n[+] Scanning finished. Check the JSON reports for details.")

if __name__ == "__main__":
    main()
