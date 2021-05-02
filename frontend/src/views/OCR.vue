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
            <v-btn @click="onUpload">Extrair texto</v-btn>
        </div>
        <div class="mt-3">
            <b-alert v-if="mostra_ocr" show>{{ resp.ocr }}</b-alert>
        </div>
    </div>
</template>




<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                imageData: [],
                files: [],
                resp: {
                    ocr: "",
                    status: 0
                }, 
                mostra_ocr: false
            }
        },
        methods: {
            onUpload() {
                console.log("upload")
                let formData = new FormData();
                formData.append('file', this.imageData);
                axios.post(
                    "http://localhost:5000/ocr",
                    formData,
                    { headers: { "Content-Type": "multipart/form-data" } }
                )
                    .then(res => {
                        this.resp.ocr = res.data.resposta
                        this.mostra_ocr = true
                    })
                    .catch(error => {
                        console.error(error);
                    })                
            },
            submitFiles() {
                if (this.files) {
                    let formData = new FormData();

                    // files
                    for (let file of this.files) {
                        formData.append("files", file, file.name);
                    }

                    // additional data
                    formData.append("test", "foo bar");

                    axios
                        .post("http://localhost:5000/ocr", formData)
                        .then(response => {
                            this.resp.ocr = res.data.resposta
                            console.log("Success!");
                            //console.log({ response });
                        })
                        .catch(error => {
                            console.log({ error });
                        });
                } else {
                    console.log("there are no files.");
                }
            }
        }
            
    };
</script>
