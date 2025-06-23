import json
import os

def generate_tf_from_forecast(forecast_json, output_dir="terraform/generated_tf_files"):
    with open(forecast_json) as f:
        forecast = json.load(f)
    
    tf_lines = [
        'provider "aws" {\n  region = "us-east-1"\n}\n'
    ]

    for ts, count in forecast.items():
        tf_lines.append(f'''
resource "aws_instance" "auto_{ts.replace(':','_').replace('-','_')}" {{
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  count         = {count}
}}
''')

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "autoscaling.tf")
    with open(output_path, "w") as f:
        f.write("\n".join(tf_lines))
    print(f"[+] Terraform file saved to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--forecast", required=True)
    parser.add_argument("--out", default="terraform/generated_tf_files")
    args = parser.parse_args()
    generate_tf_from_forecast(args.forecast, args.out)
