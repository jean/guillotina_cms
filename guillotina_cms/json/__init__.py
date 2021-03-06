from guillotina import configure
from guillotina.interfaces import IResource
from guillotina.interfaces import Interface
from guillotina.interfaces import IResourceSerializeToJsonSummary
from guillotina.interfaces import IAbsoluteURL
from guillotina.json.serialize_value import json_compatible


@configure.adapter(
    for_=(IResource, Interface),
    provides=IResourceSerializeToJsonSummary)
class DefaultJSONSummarySerializer(object):
    """Default ISerializeToJsonSummary adapter.

    Requires context to be adaptable to IContentListingObject, which is
    the case for all content objects providing IResource.
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    async def __call__(self):

        summary = json_compatible({
            '@id': IAbsoluteURL(self.context)(),
            '@type': self.context.type_name,
            'title': self.context.title
        })
        return summary