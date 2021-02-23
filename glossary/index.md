---
---

<dl class="glossary">
{% for entry in site.data.glossary %}
<dt class="glossary" id="{{ entry.key }}">{{ entry.term }}</dt>
<dd class="glossary">{{ entry.def | markdownify }}</dd>
{% endfor %}
</dl>
