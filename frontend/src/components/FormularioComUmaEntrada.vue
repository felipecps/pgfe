<template>
    <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados">
        <p class="text-break">
            {{texto_introdutorio}}
        </p>

        <b-form>
            <b-form-group id="input-exercicio" :label="label_do_exercicio" label-for="input-exercicio">
                <b-form-input id="input-1"
                              autocomplete="off"
                              v-model="form.nro1"
                              :placeholder="placeholder"
                              required></b-form-input>
            </b-form-group>

            <b-button class="mr-1" type="submit" variant="primary">{{ texto_do_botao_submit }}</b-button>
            <b-button type="reset" variant="danger" :disabled='"mostra_resposta" && form.nro1==""'>{{ texto_do_botao_reset }}</b-button>
        </b-form>

    </div>
</template>

<script>
    export default {
        props: {
            texto_introdutorio: { type: String, required: true },
            texto_do_botao_submit: { type: String, required: true },
            texto_do_botao_reset: { type: String, required: true },
            mostrar_campos_para_entrada_de_dados: { type: Boolean, required: true },
            mostra_resposta: { type: Boolean, required: true },
            label_do_exercicio: { type: String, required: true },
            placeholder: { type: String, required: true },
        }, //"mostra_resposta"
        data() {
            return {
                form: {
                    nro1: ''
                }
            }
        }
    }
</script>