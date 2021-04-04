<template>
    <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados">
        <p class="text-break">
            {{texto_introdutorio}}
        </p>

        <b-form @submit="onSubmit" @reset="onReset">
            <b-form-group id="input-exercicio" :label="label_do_exercicio" label-for="input-exercicio">
                <b-form-input id="input-1"
                              autocomplete="off"
                              v-model="form.nro1"
                              :placeholder="placeholder"
                              required></b-form-input>
            </b-form-group>

            <b-button class="mr-1" type="submit" variant="primary">{{ texto_do_botao_submit }}</b-button>
            <b-button type="reset" variant="danger" :disabled='!mostra_resposta && form.nro1==""'>{{ texto_do_botao_reset }}</b-button>
        </b-form>
        <b-alert class="mt-3" v-if="mostra_resposta" show>{{intro_resposta}} {{ resposta }} {{ m2 }}</b-alert>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: {
            texto_introdutorio: { type: String, required: true },
            texto_do_botao_submit: { type: String, required: true },
            texto_do_botao_reset: { type: String, required: true },
            mostrar_campos_para_entrada_de_dados: { type: Boolean, required: true },
            label_do_exercicio: { type: String, required: true },
            placeholder: { type: String, required: true },
            numero_do_exercicio: { type: String, required: true }
        }, 
        data() {
            return {
                form: {
                    nro1: ''
                },
                resposta: '',
                status: '',
                intro_resposta: '',
                m2: '',
                mostra_resposta: false         
            }
        },
        methods: {

            onSubmit(event) {
                event.preventDefault()
                console.log('OnSubmited')
                const path = 'http://localhost:5000/resolve_exercicios'
                //const path = 'https://felipecps.pythonanywhere.com/resolve_exercicios'
                console.log(this.numero_do_exercicio)
                if (this.form.nro1 != '') {
                    axios.post(
                        path,
                        null,
                        {
                            params: {
                                exercicio: this.numero_do_exercicio,
                                valor1: this.form.nro1
                            }
                        })
                        .then((res) => {
                            this.resposta = res.data.resposta
                            this.$emit("abc", this.resposta)
                            console.log(this.resposta)
                            this.status = res.data.status
                            if (this.status == 200) {
                                this.intro_resposta = "A área do circulo é: "
                                this.m2 = "m²"
                            } else {
                                this.intro_resposta = "",
                                    this.m2 = ""
                            }
                            this.mostra_resposta = true

                        })
                        .catch((error) => {
                            console.error(error);
                        })
                }
            },
            onReset(event) {
                event.preventDefault()
                this.form.nro1 = '',
                this.mostra_resposta = false
            }
        }
    }
</script>