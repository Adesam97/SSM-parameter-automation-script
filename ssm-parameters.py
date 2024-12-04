import os
import subprocess
from dotenv import load_dotenv

def create_ssm_parameters(env_file_path, kms_key_id=None):
    """
    Read .env file and create SSM parameters using AWS CLI
    
    Args:
        env_file_path (str): Path to the .env file
        kms_key_id (str, optional): KMS Key ID for encryption
    """
    load_dotenv(env_file_path)
    
    for key, value in os.environ.items():
        # Skip system environment variables
        if key.startswith(('PATH', 'HOME', 'USER')):
            continue
        
        try:
            # Base AWS CLI command
            cmd = [
                'aws', 'ssm', 'put-parameter',
                '--name', key,
                '--value', str(value),
                '--type', 'SecureString',
                '--tier', 'Standard',
                '--overwrite'
            ]
            
            # Add KMS Key ID if provided
            if kms_key_id:
                cmd.extend(['--key-id', kms_key_id])
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Successfully created parameter: {key}")
            else:
                print(f"Error creating parameter {key}: {result.stderr}")
        
        except Exception as e:
            print(f"Exception creating parameter {key}: {e}")

if __name__ == "__main__":

    kms_key_id = 'alias/aws/ssm'  # Replace with your KMS Key ID if needed
    create_ssm_parameters('.env', kms_key_id)