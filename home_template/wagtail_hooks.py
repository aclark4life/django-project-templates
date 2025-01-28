from wagtail import hooks

@hooks.register("insert_editor_js")
def add_objectid_js():
    return """
    <script src="{% static 'js/bson_adapter.js' %}"></script>
    """
