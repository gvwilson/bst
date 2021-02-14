---
title: "Glossary"
---

<dl>
{% for entry in site.data.glossary %}
<dt id="{{ entry.key }}">{{ entry.term }}</dt>
<dd>{{ entry.def | markdownify }}</dd>
{% endfor %}
</dl>

{% include links.md %}
