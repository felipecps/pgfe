<template>
   <div class="container">
      <b-form @submit="onSubmit" @reset="onReset" >
         <b-form-group id="input-group-1" label="Digite o Lembrete:" label-for="input-texto">

            <b-row>
               <b-col sm="10">
                  <b-form-textarea
                     id="input-texto"
                     placeholder="Texto"
                     rows="3"
                     v-model="form.text"
                     max-rows="8"
                     ></b-form-textarea>
               </b-col>
            </b-row>
         </b-form-group>

         <b-form-group class="mt-3" id="input-group-assunto" label="Assunto:" label-for="input-assunto">
            <b-form-input
               id="input-assunto"
               v-model="form.subject"
               placeholder="Sobre o que é esse lembrete?"
            ></b-form-input>
         </b-form-group>
         
         
         <b-form-group class="mt-5" id="input-group-4" description="O lembrete vai ser enviado para os emails selecionados.">
            <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
               <b-form-checkbox value="felipePessoal">f@gm</b-form-checkbox>
               <b-form-checkbox value="felipeTrabalhoSs">f.x@ss</b-form-checkbox>
               <b-form-checkbox value="felipeTrabalhoSd">f.xa@sd</b-form-checkbox>
               <b-form-checkbox value="fernandaPessoal">F.R@gm</b-form-checkbox>
               <b-form-checkbox value="fernandaTrabalho">Fernanda@K.</b-form-checkbox>
            </b-form-checkbox-group>
         </b-form-group>
         
         <br>
         <b-button class = "mr-1" type="submit" variant="primary">Submit</b-button>
         <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
   </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'EmailAlert',
  data() {
    return {
        form: {
            text: '',
            subject: '',
            checked: [],
        },
    };
  },
  methods: {
    onSubmit(evt) {
        evt.preventDefault()
        //alert(JSON.stringify(this.form))
        const listOfChecked = this.form.checked.toString()
        //alert(this.form.subject)
        //const path = 'http://localhost:5000/envia_email'
        const path = 'https://felipecps.pythonanywhere.com/envia_email'
        axios.post(
            path, 
            null, 
            {
                params: {
                    text: this.form.text,
                    subject: this.form.subject,
                    checked: listOfChecked
                }
            })
        .then((res) => {
         this.resetAllFields()
          console.log(res.data)
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    resetAllFields(){
        this.form.text = ''
        this.form.checked = []
        this.form.subject = ''
    },
    onReset(evt) {
       evt.preventDefault()
       this.resetAllFields()
      }
  },
  created() {
    
  },
};
</script>
