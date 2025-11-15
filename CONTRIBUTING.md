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
4. **Check the authorization box** - Confirm you have permission to register
5. Submit the issue

> **💡 Note**: The bot will automatically validate all technical requirements (pyproject.toml, README, CLI commands, license). You only need to confirm your authorization to register the speckit.

> **💡 Label**: Issues created using the template should automatically receive the `registration` label. If you create an issue manually or the label is missing, the bot will automatically add it when your issue title starts with `[Register]`.

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

### Package Name Uniqueness ⚠️

**Package names must be unique across all registered speckits.**

- ✅ `api-spec-kit` (first to register)
- ❌ `api-spec-kit` (duplicate - will be rejected)
- ✅ `acnet-api-spec-kit` (unique with org prefix)
- ✅ `rest-api-spec-kit` (more specific name)

**Why uniqueness matters:**
- **PyPI requires unique package names** - Only one package can use a name on PyPI
- **Prevents CLI command conflicts** - Avoids confusion when installing multiple speckits
- **Improves discoverability** - Users can easily find and identify speckits

**If your desired name is taken:**
1. **Add an organization prefix**: `myorg-package-name`, `yourname-package-name`
2. **Be more specific**: `rest-api-validator` instead of `api-validator`
3. **Add a qualifier**: `package-name-pro`, `advanced-package-name`, `package-name-toolkit`

The validation bot will automatically check for name conflicts and provide suggestions if your chosen name is already registered.

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

## 🔍 What Makes a Speckit "Spec-Driven"?

Before submitting, understand what "Spec-Driven" means:

### Core Essence of "Spec-Driven"

**Spec-Driven = Specifications Drive AI to Generate Content**

In the AI era, "Spec-Driven" means:

**Specifications → Drive AI → Generate Content**

1. **Specification as AI Input**
   - You write formal specifications (what you want)
   - Specifications provide clear intent and constraints
   - Specs are structured for AI to understand

2. **AI as the Generator**
   - AI reads and interprets specifications
   - AI generates content based on specs (code, docs, designs, protocols, configs, tests, etc.)
   - AI adapts to spec changes automatically

3. **Specification as Validator**
   - Specs validate AI-generated content
   - Ensure AI output conforms to specifications
   - Specs provide quality control and consistency

4. **The Spec-Driven Loop**
   ```
   Human Intent → Specification → AI Generation → Validation → Output
                       ↑                                          |
                       └──────────── Feedback ────────────────────┘
   ```

**Key Insight**: Specs don't just describe - they **actively drive** AI to generate what you need.

### Spec-Driven X (SD-X) - AI Generates Anything

"Spec-Driven X" means: **Specs → AI → X (Any Content)**

The "X" is a variable representing any domain where specifications can drive AI generation. Common examples:

- **SD-Development** - Specs → AI → Code, tests, implementations
- **SD-Design** - Specs → AI → UI designs, architectures
- **SD-Protocol** - Specs → AI → Protocol definitions, standards
- **SD-Documentation** - Specs → AI → Docs, guides, tutorials
- **SD-API** - API specs → AI → Client SDKs, server stubs
- **SD-Config** - Config specs → AI → System configurations
- **SD-Test** - Test specs → AI → Test cases, scenarios

**This is not a fixed taxonomy.** New categories like SD-Security, SD-Infrastructure, SD-Analytics, or any other "SD-X" can emerge. If your toolkit uses specs to drive AI content generation, it qualifies regardless of category.

### Common Applications (Examples of SD-X)

While "Spec-Driven" principle remains the same, it applies to different domains:

**Spec-Driven Specification (SDS)**
- Define protocols, standards, APIs from high-level requirements
- Example: GitHub Spec-Kit (constitution → spec), API designers

**Spec-Driven Development (SDD)**  
- Generate code, docs, tests from specifications
- Example: OpenAPI generators, Protocol Buffer compilers

**Spec-Driven Validation (SDV)**
- Validate content/behavior against specifications
- Example: Schema validators, API conformance checkers

**Spec-Driven X (SD-X)**
- SD-API, SD-Config, SD-Protocol, SD-Documentation...
- Any domain where specs drive automation

### ✅ To Qualify as "Spec-Driven", Your Tool Must:

1. **Have Formal Specifications**
   - Clear, structured specification format (not just config files)
   - Machine-readable and processable
   - Well-defined schema or structure

2. **Specs Must DRIVE (Not Just Describe)**
   - Specs generate, validate, or transform content
   - Changing the spec changes the output
   - Specs are the authority, not an afterthought

3. **Enable Automation**
   - Specs automate tasks that would otherwise be manual
   - Repeatable and consistent results from the same spec
   - Same spec can drive multiple outputs

4. **Specs as Single Source of Truth**
   - Specs can be versioned, shared, and reused
   - Specs serve as contract between components
   - Implementation derives from specs, not vice versa

### ❌ NOT Spec-Driven:

- **Config file readers** - Just parse config, don't generate from specs
- **Template engines** - Templates without formal specs
- **Manual code generators** - Human writes code, not spec-driven
- **Generic converters** - Format conversion without spec definitions
- **Simple parsers** - Parse without spec-based generation/validation

### 📚 Resources

**Reference Projects** - Learn from these spec-driven projects:
- [GitHub Spec-Kit](https://github.com/github/spec-kit) - Official Spec-Driven Development toolkit (46.6k+ stars)
- [MetaSpec](https://github.com/ACNet-AI/MetaSpec) - Meta-specification framework for generating speckits
- [Example Speckit Metadata](./examples/example-speckit.json) - Required metadata format for registration

**Documentation:**
- [MetaSpec Documentation](https://github.com/ACNet-AI/MetaSpec/tree/main/docs) - If you choose to use MetaSpec
- [Creating a Speckit with MetaSpec](https://github.com/ACNet-AI/MetaSpec/blob/main/docs/quickstart.md)

**Building from scratch?** Just ensure your speckit:
- Has a CLI interface with clear commands
- Follows spec-driven principles (specs drive generation/validation)
- Has good documentation (README with examples)
- Includes an open source license

### 💡 Quick Self-Test

Ask these four questions about your toolkit:

1. **Is there a formal spec?** → Clear, structured specification format
2. **Does the spec DRIVE?** → Spec generates/validates, not just configures  
3. **Spec → Output relationship?** → Changing spec changes output
4. **Is spec the authority?** → Everything derives from specification

**All four "YES"** = Spec-Driven ✅  
**Any "NO"** = Not spec-driven ❌

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
   - ✅ **Spec-Driven** (Most Important!):
     - Has clear specification format
     - Specs drive generation/validation/transformation
     - Changing spec changes output
     - Specs are the single source of truth
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

- ❌ **Not truly spec-driven** - Most common reason:
  - Just reads config files (not specs)
  - Template engine without formal specs
  - Specs don't drive the output
  - No clear specification format
  - See [What Makes a Speckit "Spec-Driven"?](#-what-makes-a-speckit-spec-driven) above
- ❌ **Malicious code or security concerns**
- ❌ **Incomplete or missing documentation**
- ❌ **License incompatibility** (not open source)
- ❌ **Spam or low-quality submission**
- ❌ **Duplicate of existing speckit**

### Appeals & Questions

If your submission is rejected or you have questions:
- Comment on your registration issue
- Open a discussion thread
- Contact maintainers through GitHub

We're happy to help improve submissions to meet requirements!

## 🔄 Updating Your Speckit

Have you already registered your speckit and need to update it? No problem! Our system makes updates just as easy as initial registration.

### Why Update?

You might need to update your speckit entry when:
- 🎉 **New version released** - Update version number
- 📝 **Description improved** - Better explain what your speckit does
- 🏷️ **Tags changed** - Add or modify keywords
- 🔧 **CLI commands updated** - New or renamed commands
- 📄 **License changed** - Updated license information

### What Gets Updated?

The following fields will be automatically updated from your `pyproject.toml`:
- ✅ `version` - Package version
- ✅ `description` - Project description
- ✅ `cli_command` - CLI commands from `[project.scripts]`
- ✅ `license` - License information
- ✅ `tags` - Keywords from your project
- ✅ `updated_at` - Automatically set to current date

**Note**: The `created_at` date will be preserved from your original registration.

### Method 1: Via Automated System (Recommended for Python Projects)

This is the easiest way to update your registered speckit:

#### Step 1: Update Your Repository

First, update the information in your `pyproject.toml`:

```toml
[project]
name = "my-speckit"
version = "2.0.0"  # ← Update version
description = "New improved description"  # ← Update description
keywords = ["api", "validation", "new-tag"]  # ← Update tags

[project.scripts]
my-speckit = "my_speckit.cli:main"
```

Commit and push these changes to your GitHub repository.

#### Step 2: Submit Update Issue

1. Go to [**Create Registration Issue**](../../issues/new?template=register-speckit.yml)
2. Fill in your speckit's GitHub repository URL (same as original registration)
3. Confirm your authorization (required checkbox)
4. Submit the issue

#### Step 3: Automated Update

Our bot will:
- ✅ Detect that your speckit is already registered
- ✅ Fetch the updated `pyproject.toml`
- ✅ Compare with the existing entry
- ✅ Create a PR with title: `chore: update your-speckit to v2.0.0`
- ✅ Show what changed in the PR description

#### Step 4: Review and Merge

- The PR will show exactly what changed (version, description, tags, etc.)
- Maintainers will review and merge (typically within 1-3 days)
- Your registry entry will be updated!

### Method 2: Manual Update (For All Projects)

If you prefer manual control or your project is not in Python:

#### Step 1: Fork and Clone

```bash
# If you haven't already
git clone https://github.com/YOUR_USERNAME/awesome-spec-kits.git
cd awesome-spec-kits
```

#### Step 2: Find and Update Your Entry

Open `speckits.json` and find your speckit by name:

```json
{
  "name": "my-speckit",
  "version": "1.0.0",  // ← Update this
  "description": "Old description",  // ← Update this
  "repository": "https://github.com/username/my-speckit",
  "pypi_package": "my-speckit",
  "cli_command": "my-speckit",
  "license": "MIT",
  "tags": ["api", "validation"],  // ← Update this
  "created_at": "2025-11-01",  // ← Keep this unchanged
  "updated_at": "2025-11-01",  // ← Update to today
  "status": "active"
}
```

Update the fields you want to change, and **always update** `updated_at` to the current date.

#### Step 3: Create Pull Request

```bash
# Create a branch
git checkout -b update-my-speckit

# Commit your changes
git add speckits.json
git commit -m "chore: update my-speckit to v2.0.0"

# Push and create PR
git push origin update-my-speckit
```

In your PR description, explain what you updated and why.

### Update Best Practices

#### DO ✅
- **Update `pyproject.toml` first** before submitting update issue
- **Increment version number** following semantic versioning
- **Improve descriptions** to be more searchable and clear
- **Add relevant tags** that users might search for
- **Test your CLI** to ensure commands still work

#### DON'T ❌
- **Don't change `created_at`** - This is your original registration date
- **Don't forget `updated_at`** - Always update to current date
- **Don't change `name`** - Package name should remain consistent
- **Don't change `repository`** - Repository URL should not change

### Frequency of Updates

How often should you update?

- **Major releases** - Always update (e.g., v1.0.0 → v2.0.0)
- **Minor releases with new features** - Recommended (e.g., v1.1.0 → v1.2.0)
- **Patch releases** - Optional (e.g., v1.0.1 → v1.0.2)
- **Description/tags improvements** - Anytime you have better wording

### Troubleshooting Updates

#### "Bot says speckit not found"

**Problem**: You're trying to update but bot treats it as new registration.

**Solution**: Ensure the `name` field in your `pyproject.toml` exactly matches the registered name. Package names are case-sensitive.

#### "Changes not reflected"

**Problem**: Updated `pyproject.toml` but PR shows old information.

**Solution**: 
1. Ensure changes are committed and pushed to GitHub
2. Wait a few minutes for GitHub to update the raw file
3. Try submitting the update issue again

#### "Version conflict"

**Problem**: Your new version is lower than the registered version.

**Solution**: Ensure you're incrementing the version number, not decrementing. Follow semantic versioning: `MAJOR.MINOR.PATCH`

### Quick Reference

Update workflow in 3 simple steps:

```bash
# 1. Update pyproject.toml (version, description, tags, etc.) and push
vim pyproject.toml && git commit -am "chore: bump version" && git push

# 2. Submit registration issue with same repository URL
# → https://github.com/ACNet-AI/awesome-spec-kits/issues/new?template=register-speckit.yml

# 3. Bot auto-detects update and creates PR with changes
```

That's it! The system handles everything else automatically.

### Need Help?

If you encounter issues updating your speckit:
- Comment on your update issue
- Check the [Common Issues](#-common-issues) section
- Open a discussion thread
- Contact maintainers

We're here to help make updates smooth and easy!

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

## 💬 Questions?

- **Issues**: Open an issue for questions or problems
- **Discussions**: Join community discussions
- **Documentation**: See [MetaSpec docs](https://github.com/ACNet-AI/MetaSpec)

## 🤝 Code of Conduct

Be respectful, constructive, and collaborative. We welcome contributions from everyone.

---

**Thank you for contributing to Awesome Spec Kits!** 🎉
