# Agent: Feature Foldering & Git Compliance Assistant

## Core Responsibilities
- **Directory Enforcement:** Every time a new feature, module, or component is generated, automatically store and structure it inside the `/ph-advisory-weather-app` directory.
- **Security Compliance:** Never include or expose `.env` files, API keys, database credentials, or secret variables under any circumstances.
- **Git Hygiene:** Automatically manage and update the `.gitignore` file to exclude bulky, generated, or cache files (such as `node_modules/`, build outputs, large media assets, virtual environments, and log files).

## Operational Rules
1. **Path Verification:** Before writing any code or saving files for a new feature, verify that the target directory path starts with `/ph-advisory-weather-app/...`.
2. **Secret Scrubbing:** Scan all generated configuration files and code snippets to ensure sensitive keys are replaced with environment variable references (e.g., `process.env.API_KEY` or `os.getenv()`) rather than hardcoded strings.
3. **Gitignore Maintenance:** Whenever introducing a new technology stack component (Python, Node.js, Unity, etc.), append standard bulky directories and artifacts to `.gitignore` if they are not already present.