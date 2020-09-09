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

    def blog_builder(self):
        """Creates individual blog posts"""
        blog_template = self.env.get_template("blog_layout.html")
        main_blog_template = self.env.get_template("blog_main.html")
        all_blog_posts = []
        for blog_entry in os.listdir("content/blog/"):
            blog_data = {}
            with open(f"content/blog/{blog_entry}", "r") as blog_post:
                parsed_md = markdown(blog_post.read(), extras=["metadata", "fenced-code-blocks"])
            blog_data.update({"content": parsed_md})
            blog_data.update({**blog_data, **parsed_md.metadata})
            # print(parsed_md)
            print(blog_data)
            blog_html = blog_template.render(blog=blog_data)
            print(blog_html)
            blog_file_path = f'posts/{blog_data["slug"]}.html'
            os.makedirs(os.path.dirname(blog_file_path), exist_ok=True)
            with open(blog_file_path, 'w') as file:
                file.write(blog_html)
            all_blog_posts.append(blog_data)
        sorted_blog_posts = sorted(
            all_blog_posts,
            key=lambda k: datetime.strptime(k["date"], "%Y/%m/%d"),
            reverse=True,
        )
        main_blog_html = main_blog_template.render(blog_posts=sorted_blog_posts)
        with open("blog.html", "w") as file:
            file.write(main_blog_html)
        print(main_blog_html)

    def index_builder(self):
        """Creates index.html to piece everything together"""

if __name__ == "__main__":
    builder = WebsiteBuilder()
    builder.cv_builder()
    builder.blog_builder()
