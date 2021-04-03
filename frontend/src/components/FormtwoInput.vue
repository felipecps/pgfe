<template>
    <div>
        <p class="text-break">
            {{texto}}
        </p>

        <div class="mt-3" v-if="mostrar_campos_para_entrada_de_dados_ex6">
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group id="input-exercicio-6" label="Digite o raio do círculo em metros:" label-for="input-1">
                    <b-form-input id="input-1"
                                  autocomplete="off"
                                  v-model="form.nro1"
                                  placeholder="Valor em Metros"
                                  required></b-form-input>
                </b-form-group>

                <b-button class="mr-1" type="submit" variant="primary">Calcular área do círculo</b-button>
                <b-button type="reset" variant="danger" :disabled="(mostra_resposta == false && form.nro1 == '')">Limpar</b-button>
            </b-form>
            <b-alert class="mt-3" v-if="mostra_resposta" show>{{ intro_resposta }} {{ resposta06 }} {{ m2 }}</b-alert>
        </div>


    </div>
</template>

<script>
    export default {
        props: {
            texto: { type: String, required: true }
        },
    }
</script>