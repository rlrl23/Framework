from jinja2 import Template
import datetime

def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as f:

        template = Template(f.read())

        return template.render(**kwargs)

if __name__ == '__main__':
    object_list={'year': '2023'}
    output_test = render('C:/Users/rlrl2/PycharmProjects/Frameworks/templates/index.html', context={'year': '2023'})
    #print(output_test)
    print(str(datetime.datetime.now().year))