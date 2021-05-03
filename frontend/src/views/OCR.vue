<template>
    <div class="container">
        <div>
            <b-img :src="require('../assets/OCR_2.png')" fluid alt="Responsive image"></b-img>
        </div>

        <!-- Styled -->
        <div class="mt-3">
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-file v-model="file1"
                             :state="Boolean(file1)"
                             placeholder="Escolha uma imagem ou solte-a  aqui..."
                             drop-placeholder="Solte o arquivo aqui..."></b-form-file>
                <div class="mt-3">Arquivo selecionado: {{ file1 ? file1.name : '' }}</div>

                <div class="mt-3">
                    <b-button class="mr-1" type="submit" variant="primary" :disabled="!file1">Extrair texto</b-button>
                    <b-button type="reset" variant="danger" :disabled="!file1 && !spin">Limpar</b-button>
                </div>
            </b-form>

            <div class="mt-3" v-if="mostra_ocr">
                <b-alert show>{{ texto_ocr }}</b-alert>
            </div>


            <div class="text-center mt-3" v-if="spin">
                <b-spinner v-for="variant in variants"
                           :variant="variant"
                           :key="variant"></b-spinner>
            </div>
        </div>
    </div>
</template>

<script>
    
    import Tesseract from 'tesseract.js';
    export default {
        data() {
            return {
                file1: null,
                variants: ['info'],
                texto_ocr: "",
                mostra_ocr: false,
                spin: false,
            }
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault()
                console.log(this.file1)
                this.texto_ocr = ""
                this.spin = true
                this.mostra_ocr = false
                
                Tesseract.recognize(
                    this.file1,
                    'eng',
                    {   
                        logger: m => console.log(m),
                    }
                ).then(({ data: { text } }) => {
                    this.spin = false
                    this.texto_ocr = text
                    this.mostra_ocr = true
                })
                .catch((error) => {
                    console.error(error);
                    this.texto_ocr = error
                    this.mostra_ocr = true
                })
            },
            onReset(event) {
                event.preventDefault()
                this.spin = false
                this.mostra_ocr = false
                this.texto_ocr = ""
                this.files = []
            }
        }
    }
</script>