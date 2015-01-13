from django.template.loader import render_to_string


def button_for_modal(text, url):
    return render_to_string(
        'prototypes/modal.html', {
            "buttontext": text,
            "buttonurl": url
        })


def elastic_grid(template, object_list, name):
    return render_to_string(
        template, {
            "name": name,
            "object_list": object_list,
        }
    )


def piece_of_information(label, value):
    return render_to_string("prototypes/piece_of_information.html",
                            {"label": label, "value": value})

