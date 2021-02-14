---
root: .
---
<ol>
{% for entry in site.chapters -%}
  {%- if entry.appendix -%}{%- break -%}{%- endif -%}
  <li><a href="{{ entry.slug | prepend: './' | append: '/' }}">{{ entry.title }}</a></li>
{%- endfor %}
</ol>

{% assign appendix = false %}
<ol type="A">
{% for entry in site.chapters -%}
  {%- if appendix -%}<li><a href="{{ entry.slug | prepend: './' | append: '/' }}">{{ entry.title }}</a></li>{%- endif -%}
  {%- if entry.appendix -%}{%- assign appendix = true -%}{%- endif -%}
{%- endfor %}
</ol>
