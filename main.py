import os
from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown2 import markdown
import yaml
from pathlib import Path

# for post in POSTS:
#     post_metadata = POSTS[post].metadata

#     post_data = {
#         'content': POSTS[post],
#         'title': post_metadata['title'],
#         'date': post_metadata['date']
#     }

#     post_html = post_template.render(post=post_data)
#     post_slug = post_metadata['slug']
#     post_file_path = f'output/posts/{post_slug}.html'

#     os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
#     with open(post_file_path, 'w') as file:
#         file.write(post_html)


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
        all_jobs = {}
        cv_template = self.env.get_template('cv.html')
        for cv_entry in os.listdir("content/cv/"):
            with open(f'content/cv/{cv_entry}', 'r') as job:
                parsed_md = markdown(job.read(), extras=["metadata"])
            all_jobs[cv_entry[:-3]] = {}
            all_jobs[cv_entry[:-3]]['content'] = parsed_md
            all_jobs[cv_entry[:-3]]['metadata'] = parsed_md.metadata

        print(all_jobs)
        cv_html = cv_template.render(contentjobs=all_jobs)

        with open('output/cv.html', 'w') as file:
            file.write(cv_html)
        print(cv_html)

if __name__ == "__main__":
    builder = WebsiteBuilder()
    # print(builder.template_dir)
    builder.cv_builder()
