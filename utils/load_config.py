import argparse
import json
import os


def load_config(app_description):
    json_config = read_json_file()

    # args_config = parse_service_args(app_description=app_description)

    # config = {**json_config, **args_config}
    config = {**json_config}

    return config


# def parse_service_args(app_description: str) -> tuple[argparse.Namespace, dict]:
#     parser = argparse.ArgumentParser(description=app_description)

#     parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
#     parser.add_argument("--port", type=int, default=8000, help="Port number")
#     parser.add_argument(
#         "--msname", type=str, default="Image_detector_yolo_v8", help="Service name"
#     )
#     parser.add_argument(
#         "--model_path", type=str, default="yolov8n.pt", help="Path to YOLOv8 model file"
#     )
#     parser.add_argument(
#         "--base_path", type=str, default="", help="Path to YOLOv8 model file"
#     )
#     parser.add_argument("--mshost", type=str, default="", help="Eureka client host")
#     parser.add_argument("--mszone", type=str, default="", help="Eureka server host")

#     return vars(parser.parse_args())


def read_json_file() -> dict:
    config_file_path = "config.json"

    if not os.path.exists(config_file_path):
        print(f"[ERROR] Config file not found: {config_file_path}")
        return {}

    try:
        with open(config_file_path, "r") as f:
            content = f.read().strip()
            if not content:
                print(f"[ERROR] Config file is empty: {config_file_path}")
                return {}

            config = json.loads(content)
            return config

    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse JSON config: {e}")
        return {}

    except Exception as e:
        print(f"[ERROR] Unexpected error reading config: {e}")
        return {}


# if __name__ == "__main__":
#     _, arg_dict = parse_service_args(app_description="")

#     print(arg_dict)
#     print(arg_dict["msname"])
