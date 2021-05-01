<template>
    <div class="container">
        <div>
            <v-file-input accept="image/png, image/jpeg, image/bmp"
                          placeholder="Imagem"
                          show-size
                          counter
                          label="Selecione uma imagem para extração de texto"
                          v-model="imageData"
                          prepend-icon="mdi-camera"></v-file-input>
            <v-btn @click="ocr">Extrair texto</v-btn>
        </div>
        <div class="mt-3">
            <b-alert v-if="mostra_ocr" show>{{ texto_ocr }}</b-alert>
        </div>
    </div>
</template>




<script>
    import axios from 'axios';
    var mylib = require('@/modulos/OCR/ocr.js');

    import Tesseract from 'tesseract.js';

    export default {
        data() {
            return {
                imageData: [],
                files: [],
                resp: {
                    ocr: "",
                    status: 0
                }, 
                mostra_ocr: false,
                texto_ocr: ""

            }
        },
        methods: {
            onUpload() {
                mylib.ocr()              
            },
            ocr() {
                Tesseract.recognize(
                    'http://127.0.0.1:8887/eng_bw.png',
                    'eng',
                    { logger: m => console.log(m) }
                ).then(({ data: { text } }) => {
                    //console.log(text);
                    this.mostra_ocr = true
                    this.texto_ocr = text
                })
            }
        }
            
    };
</script>
