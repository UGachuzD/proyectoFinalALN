<template>
  <v-container
    class="fill-height d-flex flex-column justify-center align-center"
    style="background-color: #121212; padding: 40px;"
  >
    <v-responsive
      class="align-center fill-height mx-auto px-6"
      max-width="1000"
    >
      <div class="text-center mb-8">
        <div class="text-body-2 font-weight-light mb-2" style="color: #b0b0b0; font-size: 18px;">
          Aplicaciones de Lenguaje Natural
        </div>
        <h1 class="text-h2 font-weight-bold" style="color: #ffffff; font-size: 36px;">
          Proyecto Final
        </h1>
      </div>

      <v-card
        class="py-8 px-8 d-flex flex-column align-center justify-center"
        style="box-shadow: 0px 6px 16px rgba(0, 0, 0, 0.5); border-radius: 16px; background-color: #1e1e1e; color: white; max-width: 900px; width: 100%;"
      >
        <!-- Fila del texto "Selecciona el idioma" y los radio buttons -->
        <v-row class="mb-6" style="width: 100%; color: white;">
          <v-col cols="12" md="6" class="text-center">
            <h3 class="text-h5 font-weight-bold" style="font-size: 20px;">
              Selecciona el idioma
            </h3>
          </v-col>
          <v-col cols="12" md="6" class="d-flex justify-center">
            <v-radio-group v-model="selectedLanguage" row>
              <v-radio
                label="Español"
                value="spanish"
                style="color: white; font-size: 16px;"
              ></v-radio>
              <v-radio
                label="Inglés"
                value="english"
                style="color: white; font-size: 16px;"
              ></v-radio>
            </v-radio-group>
          </v-col>

        <!-- Fila para el textarea -->
          <v-col cols="12">
            <v-textarea
              v-model="text"
              outlined
              rows="6"
              placeholder="Escribe aquí tu texto..."
              style="border-radius: 12px; background-color: #2b2b2b; color: white; font-size: 16px; padding: 16px;"
            ></v-textarea>
          </v-col>

        <!-- Fila para el botón de analizar -->
            <v-col cols="12" class="d-flex justify-center">
            <v-btn
              @click="analyzeText"
              style="padding: 14px 28px; font-size: 18px; font-weight: bold; border-radius: 8px; background-color: #4caf50; color: white; display: flex; align-items: center; justify-content: center; width: 100%;"
            >
              Analizar
            </v-btn>
            </v-col>

        <!-- Fila para el resultado -->
          <v-col cols="12" class="text-center">
            <p class="text-subtitle-1 font-weight-medium" style="font-size: 18px;">
              {{result}}
            </p>
          </v-col>
        </v-row>
      </v-card>
    </v-responsive>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const text = ref('');
const result = ref('...');
const selectedLanguage = ref('spanish');

async function analyzeText() {
  console.log('Front - Texto:', text.value);
  console.log('Front - Idioma seleccionado:', selectedLanguage.value);

  try {
    const response = await axios.post('http://127.0.0.1:5000/api/analyzeText', {
      text: text.value,
      language: selectedLanguage.value
    });
    result.value = response.data.message;
    console.log('Back - Respuesta:', result.value);
  } catch (error) {
    console.error('Error al analizar el texto:', error);
    result.value = 'Error al analizar el texto';
  }
}


</script>
