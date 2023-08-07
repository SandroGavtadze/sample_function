import subprocess
import os

def run_gcloud_command(request):
    try:
        project_id = os.environ.get("PROJECT_ID")
        region = os.environ.get("REGION")
        
        gcloud_command = f"gcloud config set project {project_id} && gcloud compute regions list --filter=\"name={region}\""
        
        result = subprocess.run(gcloud_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        
        return f"Command output: {result.stdout}"
        
    except subprocess.CalledProcessError as e:
        return f"Error executing the command: {e}\nCommand stderr: {e.stderr}"
