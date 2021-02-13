---
---
<ol>
{% for chapter in site.chapters %}
  {% if chapter.chapter %}
  <li><a href="{{ chapter.slug | prepend: './' | append: '/' }}">{{ chapter.title }}</a></li>
  {% endif %}
{% endfor %}
</ol>

<ol type="A">
{% for chapter in site.chapters %}
  {% unless chapter.chapter %}
  <li><a href="{{ chapter.slug | prepend: './' | append: '/' }}">{{ chapter.title }}</a></li>
  {% endunless %}
{% endfor %}
</ol>
