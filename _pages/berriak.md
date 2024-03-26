---
layout: default
title: GATAI
permalink: /berriak
---

<h2 class="project-tagline">X sare sozialean aurkituko gaituzu #GATAI traolarekin</h2>
<h3 class="project-tagline">Azken berriak:</h3>

<ul>
    {% for post in site.posts %}
        <li>
	    <img src="{{ post.image }}" alt="{{ post.title }}" style="width: 100px; height: auto;">
            <a href=" {{ post.url }} "> {{ post.title }} ({{ post.date | date: "%Y/%m/%d" }}) </a>
	   {{ post.excerpt }}
        </li>
    {% endfor %}
</ul>