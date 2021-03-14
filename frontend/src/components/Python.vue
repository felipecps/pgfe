<template>
    <div class="container">
        <b-form @submit="onSubmit">
            <p class="text-break">
                1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
            </p>
            <b-button class="mr-1" @click="submit('1')" variant="outline-primary">Executar</b-button>
            <b-alert class="mt-3" v-if="mostra_resposta" show>{{ resposta }}</b-alert>
        </b-form>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'PythonExercicios',
        data() {
            return {
                mostra_resposta: false,
                resposta: "",
                status: 0
            };
        },
        methods: {
            submit(nroDo_exercicio) {
                const path = 'http://localhost:5000/resolve_exercicios'
                //const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'
                axios.post(
                    path,
                    null,
                    {
                        params: {
                            exercicio: nroDo_exercicio,
                        }
                    })
                    .then((res) => {
                        this.resposta = res.data.resposta
                        this.status = res.data.status
                        if (this.status = 200) {
                            this.mostra_resposta = true
                        }
                        //alert(this.resposta)
                    })
                    .catch((error) => {
                        console.error(error);
                    })
            },
            onSubmit(evt) {
                evt.preventDefault()

            }
        },
        created() {

        },
    };
</script>
