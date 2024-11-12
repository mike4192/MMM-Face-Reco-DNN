import argparse

ap = argparse.ArgumentParser()

ap.add_argument(
            "-roon",
            "--run-only-on-notification",
            type=int,
            default=0,
            help="If set to 1, only runs face detection upon externally provided trigger via HTTP POST.",
        )

print(vars(ap.parse_args()))