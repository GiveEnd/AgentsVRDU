import json
import subprocess


def parse_pdf(pdf_path: str) -> dict:

    result = subprocess.run(
        [
            "lit",
            "parse",
            pdf_path,
            "--format",
            "json",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    

    return json.loads(result.stdout)

# if __name__ == "__main__":
#     document = parse_pdf(
#         "/app/data/input/test.pdf"
#     )

#     print(
#         f"Pages: {len(document.get('pages', []))}"
#     )