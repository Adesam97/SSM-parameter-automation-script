# SSM-parameter-automation-script

# AWS SSM Parameter Store Automation

## Overview
This repository contains scripts to automate the creation of AWS Systems Manager (SSM) Parameters from a local `.env` file. The automation supports both Python and Bash implementations for flexible parameter store management.

## Prerequisites

### AWS Requirements
- AWS Account
- IAM User with permissions to create SSM Parameters
- AWS CLI installed and configured

### System Requirements
- Python 3.7+ (for Python script)
- Bash (for Bash script)
- AWS CLI
- `awscli` Python package

### Configuration

1. **AWS Credentials**
   Configure your AWS credentials using one of the following methods:
   - AWS CLI: `aws configure`
   - Environment variables:
     ```
     export AWS_ACCESS_KEY_ID=your_access_key
     export AWS_SECRET_ACCESS_KEY=your_secret_key
     export AWS_DEFAULT_REGION=your_preferred_region
     ```
   - AWS Credentials file (`~/.aws/credentials`)

2. **Environment File**
   Create a `.env` file in the repository root with your key-value pairs:
   ```
   DB_USERNAME=mydbuser
   DB_PASSWORD=mysecretpassword
   API_KEY=myapikey
   ```

   > **Note:** Ensure `.env` is added to `.gitignore` to prevent accidental exposure of sensitive information.

## Scripts

### 1. Python Script (`ssm-parameters.py`)

#### Features
- Reads parameters from `.env` file
- Creates SSM Parameters
- Supports different parameter types
- Error handling

#### Usage
```bash
python3 ssm-parameters.py
```

#### Optional Parameters
- `--type`: Specify parameter type (default: SecureString)
- `--path`: Custom SSM parameter path prefix

### 2. Bash Script (`ssm-parameters.sh`)

#### Features
- Shell-based parameter creation
- Works with standard Unix environments
- Minimal dependencies

#### Usage
```bash
chmod +x ssm-parameters.sh
./ssm-parameters.sh
```

## Best Practices

1. Use `SecureString` for sensitive parameters
2. Implement least-privilege IAM roles
3. Rotate credentials regularly
4. Use parameter hierarchy for better organization

## Security Considerations

- Never commit `.env` file to version control
- Use AWS Secrets Manager for highly sensitive credentials
- Implement encryption at rest and in transit

## Troubleshooting

- Ensure AWS CLI is properly configured
- Check IAM permissions
- Verify `.env` file format
- Use `--debug` flag for detailed error information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify your license, e.g., MIT, Apache 2.0]

## Support

For issues or questions, please open a GitHub issue in the repository.