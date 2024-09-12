---
layout: default_es
title: GATAI
permalink: /noticias
---

<h2 class="project-tagline">X sare sozialean aurkituko gaituzu #GATAI traolarekin</h2>

<div class="posts-list">

    {% for post in site.posts %}

       {% if post.lang == "es" %}
    
        <hr>

    	<div class="post">

    	  <a href=" {{ post.url }} ">

              {{ post.title }} ({{ post.date | date: "%Y/%m/%d" }})
	      
	      <img src="{{ post.image }}" alt="{{ post.title }}" class="post-image">


	  </a>
	  <p>
		{{ post.excerpt }}
	  </p>

	</div>
	
      {% endif %}
      
    {% endfor %}

</div>