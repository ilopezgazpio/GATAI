---
layout: default_es
title: GATAI
permalink: /noticias
---

<h2 class="project-tagline">Nos encontrarás en la red social X con el hashtag #GATAI</h2>

<div class="posts-list">

    {% for post in site.posts %}

       {% if post.lang == "es" %}
    
        <hr>

    	<div class="post">

    	  <a href=" {{ post.url }} ">

              {{ post.title }} ({{ post.date | date: "%d/%m/%Y" }})
	      
	      <img src="{{ post.image }}" alt="{{ post.title }}" class="post-image">


	  </a>
	  <p>
		{{ post.excerpt }}
	  </p>

	</div>
	
      {% endif %}
      
    {% endfor %}

</div>