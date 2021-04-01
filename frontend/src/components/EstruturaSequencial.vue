<template>
    <div class="container">
        <b-card border-variant="dark" header="Estrutura Sequencial" align="left">
            <div v-for="link in links">
                <b-link :href="link.nro">{{ link.texto }}</b-link>
            </div>
        </b-card>

        
    </div>
</template>


<script>
        //import TextoIntrodutorio from "@/components/TextoIntrodutorio.vue";

        export default {
            components: {
                //TextoIntrodutorio
            },
            data() {
                return {
                    links: [
                        { nro: "/python/estruturaSequencial/ex1", texto: "1. Faça um Programa que mostre a mensagem 'Alo mundo' na tela." }, 
                        { nro: "/python/estruturaSequencial/ex2", texto: "2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]." },
                        { nro: "/python/estruturaSequencial/ex3", texto: "3. Faça um Programa que peça dois números e imprima a soma." },
                        { nro: "/python/estruturaSequencial/ex4", texto: "4. Faça um Programa que peça as 4 notas bimestrais e mostre a média." },
                        { nro: "/python/estruturaSequencial/ex5", texto: "5. Faça um Programa que converta metros para centímetros." },
                        { nro: "/python/estruturaSequencial/ex6", texto: "6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área." }
                    ]
                };
            },
            methods: {
                
                onSubmit(evt) {
                    evt.preventDefault()
                },
                onReset(event) {
                    event.preventDefault()
                    
                }
            },
            created() {

            },
        };
</script>