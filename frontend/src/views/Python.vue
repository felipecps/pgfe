<template>

    <div class="container">
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="10" use-router></b-pagination-nav>
     
        <div>
            <b-list-group>
                <b-list-group-item href="/python/estruturaSequencial" class="list-group-item list-group-item-primary">Estrutura Sequencial</b-list-group-item>
                <b-list-group-item href="#" disabled>Estrutura de Decisão</b-list-group-item>
                <b-list-group-item href="#" disabled>Estrutura de Repetição</b-list-group-item>
                <b-list-group-item href="#" disabled>Exercício de Listas</b-list-group-item>
                <b-list-group-item href="#" disabled>Exercício de Funções</b-list-group-item>
                <b-list-group-item href="#" disabled>Exercício com Strings</b-list-group-item>
                <b-list-group-item href="#" disabled>Exercício de Arquivos</b-list-group-item>
                <b-list-group-item href="#" disabled>Exercício de Classes</b-list-group-item>
                <b-list-group-item href="#" disabled>Lista de Exercícios - Projetos</b-list-group-item>
            </b-list-group>
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