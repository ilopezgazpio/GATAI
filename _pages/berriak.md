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
	<p>
            <a href=" {{ post.url }} "> {{ post.title }} ({{ post.date | date: "%Y/%m/%d" }}) </a>
	</p>
	<p>
	   {{ post.excerpt }}
	</p>
        </li>
    {% endfor %}
</ul>