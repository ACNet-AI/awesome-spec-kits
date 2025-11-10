# Contributing to Awesome Spec Kits

Thank you for your interest in contributing! This guide explains how to add your speckit to the registry.

## 🌟 Open to All Implementations

**We welcome any speckit that follows spec-driven principles!** 

- ✅ **Build from scratch** - Implement your own solution without any framework
- ✅ **Use any framework** - MetaSpec, or any other framework you prefer
- ✅ **Any language** - Python, JavaScript, Go, Rust, whatever you choose
- ✅ **Adapt existing tools** - Extend or wrap existing tools to be spec-driven

As long as your toolkit embodies Spec-Driven X (SD-X) philosophy and meets our registration requirements, you're welcome!

**Note**: Our automated registration currently supports Python projects with `pyproject.toml`. For projects in other languages (Node.js, Go, Rust, etc.), please use the [manual registration process](#-manual-registration-alternative).

## 🚀 Quick Start: Automated Registration (Python Projects)

The easiest way to register your Python speckit is through our automated system:

### Step 1: Prepare Your Speckit

Ensure your speckit meets these requirements:

- ✅ Valid `pyproject.toml` with `name`, `version`, and `description`
- ✅ `README.md` with documentation
- ✅ Working CLI commands defined in `[project.scripts]`
- ✅ Open source license (MIT, Apache, BSD, etc.)
- ✅ Published to GitHub (public repository)

### Step 2: Submit Registration Issue

1. Go to [**Create Registration Issue**](../../issues/new?template=register-speckit.yml)
2. Fill in your speckit's GitHub repository URL
3. Optionally provide PyPI package name
4. Submit the issue

### Step 3: Automated Validation

Our bot will automatically:

- ✅ Fetch and validate your `pyproject.toml`
- ✅ Extract metadata (name, version, description, CLI commands)
- ✅ Verify README.md exists
- ✅ Create a Pull Request if validation passes
- ✅ Comment on the issue with results

### Step 4: Review and Merge

If validation passes:
- A PR will be created automatically
- Maintainers will review (usually within 1-3 days)
- Once merged, your speckit appears in the registry!

If validation fails:
- The bot comments with detailed error messages
- Fix the issues in your repository
- Edit the issue to trigger re-validation

## 📋 Requirements

### Required Files

Your speckit repository must have:

#### `pyproject.toml`

Must include these fields in the `[project]` section:

```toml
[project]
name = "my-speckit"
version = "1.0.0"
description = "Brief description of your speckit"

[project.scripts]
my-speckit = "my_speckit.cli:main"
```

#### `README.md`

Should include:
- Clear description of what your speckit does
- Installation instructions
- Usage examples
- License information

### Quality Standards

To ensure good user experience:

- **Clear Description**: 50-200 characters, searchable, explains purpose
- **Relevant Tags**: Keywords from your `pyproject.toml` help users find your speckit
- **Working CLI**: All commands listed should work after installation
- **Active Maintenance**: Repository should be actively maintained
- **Documentation**: Clear README with examples

### Naming Conventions

- **Package name**: Lowercase, hyphens allowed (e.g., `api-spec-kit`)
- **CLI command**: Should match package name or be intuitive
- **Repository**: Public GitHub repository with clear purpose

## 🔧 Manual Registration (Alternative)

**For all languages and frameworks** - Use this method if:
- Your project is not in Python
- You prefer manual control
- The automated system is unavailable

### Step 1: Fork and Clone

```bash
# Fork this repository
# https://github.com/ACNet-AI/awesome-spec-kits

# Clone your fork
git clone https://github.com/YOUR_USERNAME/awesome-spec-kits.git
cd awesome-spec-kits
```

### Step 2: Add Your Speckit

The registry is stored in `speckits.json`. Add your entry:

```json
{
  "name": "my-speckit",
  "version": "1.0.0",
  "description": "Brief description",
  "repository": "https://github.com/username/my-speckit",
  "pypi_package": "my-speckit",
  "cli_command": "my-speckit",
  "license": "MIT",
  "tags": ["api", "validation"],
  "created_at": "2025-11-09",
  "updated_at": "2025-11-09",
  "status": "active"
}
```

### Step 3: Create Pull Request

```bash
# Create a branch
git checkout -b add-my-speckit

# Add your changes
git add speckits.json
git commit -m "feat: add my-speckit to registry"

# Push and create PR
git push origin add-my-speckit
```

## 🔍 Validation & Review Process

Understanding how speckits are validated and reviewed:

### Automated Validation (For Python Projects)

When you submit a registration issue, our bot automatically:

1. **Fetches Your Repository**
   - Retrieves `pyproject.toml` from your repository
   - Checks for `README.md` existence
   - Validates repository accessibility

2. **Validates Required Fields**
   - ✅ `name` - Package name in `[project]`
   - ✅ `version` - Version number in `[project]`
   - ✅ `description` - Project description in `[project]`
   - ⚠️  `[project.scripts]` - CLI commands (warning if missing)
   - ⚠️  `README.md` - Documentation (warning if missing)

3. **Extracts Metadata**
   - Package name, version, description
   - CLI command names
   - License information
   - Keywords/tags from `pyproject.toml`

4. **Validation Result**
   - ✅ **Pass**: Bot creates a PR automatically
   - ❌ **Fail**: Bot comments on issue with error details

### Manual Validation (For All Projects)

For manual submissions or non-Python projects:

1. **Basic Requirements Check**
   - Has a public GitHub repository
   - Has clear documentation (README)
   - Has a CLI interface
   - Has an open source license
   - Follows spec-driven principles

2. **Metadata Completeness**
   - All required fields in `speckits.json` are filled
   - Description is clear and searchable
   - Tags are relevant

3. **Quality Assessment**
   - Documentation quality (examples, usage guide)
   - Code quality (if visible)
   - Community activity (issues, stars, commits)
   - Maintenance status (recent updates)

### Human Review Process

All registrations (automated or manual) go through human review:

1. **Maintainer Review** (1-3 days typically)
   - Verify speckit truly follows spec-driven principles
   - Check for duplicate or similar existing speckits
   - Review description clarity and accuracy
   - Ensure license compatibility
   - Check for malicious content or spam

2. **Quality Check**
   - ✅ **Spec-Driven**: Does it use specs to drive generation/validation?
   - ✅ **Usability**: Is documentation clear and helpful?
   - ✅ **Completeness**: Are all metadata fields accurate?
   - ✅ **Community Value**: Does it add value to the registry?

3. **Decision**
   - ✅ **Approve & Merge**: Speckit added to registry
   - 💬 **Request Changes**: Feedback provided, resubmission welcome
   - ❌ **Reject**: Doesn't meet requirements (with explanation)

### What Happens After Approval?

1. PR is merged into `main` branch
2. `speckits.json` is updated
3. Your speckit appears on the registry
4. Issue is automatically closed
5. You're notified of the merge

### Common Rejection Reasons

- ❌ Not truly spec-driven (specs are not the primary driver)
- ❌ Malicious code or security concerns
- ❌ Incomplete or missing documentation
- ❌ License incompatibility (not open source)
- ❌ Spam or low-quality submission
- ❌ Duplicate of existing speckit

### Appeals & Questions

If your submission is rejected or you have questions:
- Comment on your registration issue
- Open a discussion thread
- Contact maintainers through GitHub

We're happy to help improve submissions to meet requirements!

## 🔄 Updating Your Speckit

To update your speckit's metadata:

### Via Automated System

1. Update your `pyproject.toml` (version, description, etc.)
2. Create a new registration issue
3. The bot will update the existing entry

### Manual Update

1. Fork and clone (if you haven't)
2. Edit your entry in `speckits.json`
3. Update `version` and `updated_at` fields
4. Create a PR with your changes

## 🗑️ Removing Your Speckit

To remove your speckit from the registry:

1. Create an issue explaining the reason (deprecated, renamed, etc.)
2. Or submit a PR removing your entry from `speckits.json`
3. Maintainers will review and process

## 📝 Metadata Reference

The registry stores these fields for each speckit:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Package name from `pyproject.toml` |
| `version` | string | ✅ | Current version |
| `description` | string | ✅ | Brief description (50-200 chars) |
| `repository` | string | ✅ | GitHub repository URL |
| `pypi_package` | string | ✅ | PyPI package name |
| `cli_command` | string | ✅ | Main CLI command name |
| `license` | string | ✅ | License type (MIT, Apache, etc.) |
| `tags` | array | ⚠️ | Keywords for search (from `pyproject.toml`) |
| `created_at` | string | ✅ | Registration date (YYYY-MM-DD) |
| `updated_at` | string | ✅ | Last update date (YYYY-MM-DD) |
| `status` | string | ✅ | Status: "active", "deprecated", "archived" |

## 🏷️ Tag Guidelines

Use clear, searchable tags from your `pyproject.toml`:

**Domain Tags**
- `api`, `protocol`, `config`, `database`, `documentation`

**Technology Tags**
- `yaml`, `json`, `xml`, `toml`, `openapi`, `graphql`

**Function Tags**
- `validation`, `generation`, `linting`, `testing`, `conversion`

**Example**:
```toml
[project]
keywords = ["api", "validation", "openapi", "testing"]
```

## ❓ Common Issues

### Validation Failed: Missing pyproject.toml

**Problem**: Bot cannot find `pyproject.toml` in repository root

**Solution**: Ensure `pyproject.toml` exists in the root directory of your repository

### Validation Failed: No CLI Commands

**Problem**: No commands defined in `[project.scripts]`

**Solution**: Add CLI commands to your `pyproject.toml`:
```toml
[project.scripts]
my-speckit = "my_speckit.cli:main"
```

### Validation Failed: Invalid Description

**Problem**: Missing or too short description

**Solution**: Add a clear description in `pyproject.toml`:
```toml
[project]
description = "A toolkit for validating API specifications"
```

## 📚 Resources

- [Example Speckit Metadata](./examples/example-speckit.json) - Required metadata format for registration
- [MetaSpec Framework](https://github.com/ACNet-AI/MetaSpec) - Optional framework for creating speckits
- [MetaSpec Documentation](https://github.com/ACNet-AI/MetaSpec/tree/main/docs) - If you choose to use MetaSpec
- [Creating a Speckit with MetaSpec](https://github.com/ACNet-AI/MetaSpec/blob/main/docs/quickstart.md)

**Building from scratch?** No problem! Just ensure your speckit:
- Has a CLI interface with clear commands
- Follows spec-driven principles (specs drive generation/validation)
- Has good documentation (README with examples)
- Includes an open source license

## 💬 Questions?

- **Issues**: Open an issue for questions or problems
- **Discussions**: Join community discussions
- **Documentation**: See [MetaSpec docs](https://github.com/ACNet-AI/MetaSpec)

## 🤝 Code of Conduct

Be respectful, constructive, and collaborative. We welcome contributions from everyone.

---

**Thank you for contributing to Awesome Spec Kits!** 🎉
