<template>
    <div class="container">
        <div class="mt-3">
            <TextoIntrodutorio v-show="true" :texto="texto3"
                               @temp-teste="temp_teste_metodo"></TextoIntrodutorio>

            


        </div>
    </div>
</template>

<script>
    import TextoIntrodutorio from "@/components/TextoIntrodutorio.vue";

    export default {
        components: {
            TextoIntrodutorio
        },
        data() {
            return {
                texto3: "texto introdutorio",
                text: '',
                post: true,
                form: {
                    nro3: ''
                },
                mostrar_campos_para_entrada_de_dados_ex3: false,
                mostra_resposta: false,
                resposta03: "",
                status: 0
            };
        },
        methods: {
            temp_teste_metodo(abc) {
                alert(abc)
            }
        }
    }

</script>