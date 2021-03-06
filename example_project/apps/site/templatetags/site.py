import os

import CommonMark
import jinja2
from bs4 import BeautifulSoup
from cms.apps.pages.templatetags.pages import _navigation_entries
from cms.html import process as process_html
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django_jinja import library

from ..models import Footer, Header


@library.global_function
def frontend_templates():
    return mark_safe([
        str(f[:-5])
        for f in os.listdir(os.path.join(settings.TEMPLATES[0]['DIRS'][0], 'frontend'))
        if f[:1] != '_'
    ])


# Usage: get_next_by_field(obj, 'date')
@library.global_function
def get_next_by_field(obj, field):
    try:
        return getattr(obj, 'get_next_by_{}'.format(field))()
    except obj.DoesNotExist:
        return obj._default_manager.last()
    except Exception:  # pylint:disable=broad-except
        pass  # Will cause 'None' to be returned.


# Usage: get_previous_by_field(obj, 'date')
@library.global_function
def get_previous_by_field(obj, field):
    try:
        return getattr(obj, 'get_previous_by_{}'.format(field))()
    except obj.DoesNotExist:
        return obj._default_manager.first()
    except Exception:  # pylint:disable=broad-except
        pass  # Will cause 'None' to be returned.


@library.global_function
@library.render_with('pages/navigation.html')
@jinja2.contextfunction
def render_navigation(context, pages, section=None, recursive=False):
    """
    Renders a navigation list for the given pages.

    The pages should all be a subclass of PageBase, and possess a get_absolute_url() method.

    You can also specify an alias for the navigation, at which point it will be set in the
    context rather than rendered.
    """
    return {
        'navigation': _navigation_entries(context, pages, section),
        'recursive': recursive,
    }


@library.filter
def md_escaped(value, inline=True):
    if not value:
        return ""

    formatted = value.strip()

    if inline:
        formatted = formatted.replace('\n', '<br>')

    formatted = CommonMark.commonmark(formatted).strip()

    # Remove wrapping <p> tags.
    if inline and formatted.startswith('<p>') and formatted.endswith('</p>'):
        formatted = formatted[3:-4]

    return formatted


@library.filter
def md(value, inline=True):
    """
    Formats a string of Markdown text to HTML.

    By default it assumes that the text will be wrapped in a meaningful
    block-level element, i.e. the return value will not be wrapped in a `<p>`
    tag, and line breaks will be rendered using `<br>` elements. If you wish
    to override this and use standard Markdown behaviour, pass `inline=True`
    as an argument to this filter.

    This should never be used on untrusted user input, as Markdown by design
    allows arbitrary HTML.
    """
    return mark_safe(md_escaped(value, inline=inline))


@library.filter
@stringfilter
def html(text):
    # Return empty string if no text
    if not text:
        return ""

    # Process HTML through cms parser
    text = process_html(text)

    # Load text into BS4
    soup = BeautifulSoup(text, 'html.parser')

    # Unwrap all image tags
    for img in soup.find_all('img'):
        img.parent.unwrap()

    def wrap(to_wrap, wrap_in):
        contents = to_wrap.replace_with(wrap_in)
        wrap_in.append(contents)

    # Wrap all table tags
    for table in soup.find_all('table'):
        div = soup.new_tag('div')
        div['class'] = 'wys-TableWrap'
        wrap(table, div)

    # Wrap all iframes in intrinsic containers
    for iframe in soup.find_all('iframe'):
        for attr in ['width', 'height']:
            if iframe.get(attr, None):
                del iframe[attr]
        wrapper = soup.new_tag('div', **{'class': 'wys-Intrinsic'})
        iframe.wrap(wrapper)

    # Force return string version of BS4 obj
    return mark_safe(str(soup))


@library.global_function
def get_header_content():
    return Header.objects.first()


@library.global_function
def get_footer_content():
    return Footer.objects.first()
