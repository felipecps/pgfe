<template>
    <div class="container">
        <!-- Styled -->
        <div class="mt-3">
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-file v-model="file1"
                             :state="Boolean(file1)"
                             placeholder="Escolha uma imagem ou solte-a  aqui..."
                             drop-placeholder="Solte o arquivo aqui..."></b-form-file>
                <div class="mt-3">Arquivo selecionado: {{ file1 ? file1.name : '' }}</div>

                <div class="mt-3">
                    <b-button class="mr-1" type="submit" variant="primary" :disabled="!file1 && !ocr_suspenso">Extrair texto</b-button>
                    <b-button type="reset" variant="danger" :disabled="!file1 && !mostra_ocr && !spin">Limpar</b-button>
                </div>
            </b-form>

            <div class="mt-3" v-if="mostra_ocr && !ocr_suspenso">
                <b-alert show>{{ texto_ocr }}</b-alert>
            </div>


            <div class="text-center mb-3" v-if="spin">
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
                ocr_suspenso: true,
                variants: ['info'],
                resp: {
                    ocr: "",
                    status: 0
                },
                mostra_ocr: false,
                texto_ocr: "",
                spin: false,
            }
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault()
                console.log(this.file1)
                this.mostra_ocr = false
                this.ocr_suspenso = false
                this.texto_ocr = ""
                this.spin = true
                
                Tesseract.recognize(
                    this.file1,
                    'eng',
                    {   
                        logger: m => console.log(m),
                    }
                ).then(({ data: { text } }) => {
                    this.spin = false
                    this.mostra_ocr = true
                    this.texto_ocr = text
                })
            },
            onReset(event) {
                event.preventDefault()
                this.spin = false
                this.mostra_ocr = false
                this.texto_ocr = ""
                this.files = []
                this.suspenso = true
            }
        }
    }
</script>