"""Personal website and CV creator"""
import os
from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown2 import markdown
import yaml
from pathlib import Path


class WebsiteBuilder:
    """Creates my personal website"""

    def __init__(self):
        self.template_dir = None
        for config_file in os.listdir("configs"):
            self.load_config(config_file)
        self.env = Environment(
            loader=PackageLoader("main", self.template_dir),
            autoescape=select_autoescape(["html", "xml"]),
        )

    def load_config(self, config_path):
        """Loads config from yaml"""
        my_path = Path(__file__).resolve()  # resolve to get rid of any symlinks
        config_path = f"{my_path.parent}/configs/{config_path}"
        with open(config_path, "r") as file_stream:
            try:
                config = yaml.safe_load(file_stream)
                self.template_dir = config["paths"]["template"]
            except yaml.YAMLError as exc:
                print(exc)

    def cv_builder(self):
        """Gathers work experience and builds a CV"""
        all_jobs = []
        cv_template = self.env.get_template("cv_layout.html")
        for cv_entry in os.listdir("content/cv/jobs/"):
            job_data = {}
            with open(f"content/cv/jobs/{cv_entry}", "r") as job:
                parsed_md = markdown(job.read(), extras=["metadata"])
            job_data.update({"content": parsed_md})
            job_data.update({**job_data, **parsed_md.metadata})
            all_jobs.append(job_data)

        sorted_jobs = sorted(
            all_jobs,
            key=lambda k: datetime.strptime(k["start_date"], "%Y/%m/%d"),
            reverse=True,
        )
        cv_html = cv_template.render(jobs=sorted_jobs)

        with open("cv.html", "w") as file:
            file.write(cv_html)
        print(cv_html)


if __name__ == "__main__":
    builder = WebsiteBuilder()
    builder.cv_builder()
