from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class HomePage(Page):
    pass


class ProductPage(Page):
    body = StreamField([
        ('heading', blocks.RichTextBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('url', blocks.URLBlock()),
        ('datetime', blocks.DateTimeBlock()),
        ('qoute', blocks.BlockQuoteBlock()),
        ('file', DocumentChooserBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
