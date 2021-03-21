<template>
    <div class="container">
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="10" use-router></b-pagination-nav>
        <div>
            <b-link href="/estruturaSequencial">Estrutura Sequencial</b-link>
        </div>
    </div>
</template>

<script>
  export default {
    methods: {
      linkGen(pageNum) {
            return `/foo/page/${pageNum}`
      }
    }
  }
</script>