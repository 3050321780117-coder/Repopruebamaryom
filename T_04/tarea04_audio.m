# =============================================
# TAREA 04 - PROCESAMIENTO DIGITAL DE SENALES
# =============================================

if (exist('OCTAVE_VERSION', 'builtin') ~= 0)
    pkg load signal;
endif

opcion = 0;

while opcion ~= 5

    disp('Seleccione una opcion:')
    disp('1. Grabar audio')
    disp('2. Reproducir audio')
    disp('3. Graficar audio')
    disp('4. Graficar densidad espectral')
    disp('5. Salir')

    opcion = input('Ingrese su seleccion: ');

    switch opcion

        case 1

            try
                duracion = input('Ingrese la duracion de la grabacion en segundos: ');

                disp('Comenzando la grabacion...');

                # Micrófono seleccionado: ID 0
                recObj = audiorecorder(44100, 16, 1, 0);

                recordblocking(recObj, duracion);

                disp('Grabacion finalizada.');

                data = getaudiodata(recObj);

                audiowrite('audio.wav', data, recObj.SampleRate);

                disp('Archivo audio.wav guardado correctamente.');

            catch
                disp('Error al grabar el audio.');
            end_try_catch


        case 2

            try
                [data, fs] = audioread('audio.wav');

                sound(data, fs);

            catch
                disp('Error al reproducir el audio.');
            end_try_catch


        case 3

            try
                [data, fs] = audioread('audio.wav');

                tiempo = linspace(0, length(data)/fs, length(data));

                figure;

                plot(tiempo, data);

                xlabel('Tiempo (s)');
                ylabel('Amplitud');
                title('Audio grabado');

                grid on;

            catch
                disp('Error al graficar el audio.');
            end_try_catch


        case 4

            try
                disp('Graficando espectro de frecuencia...');

                [audio, Fs] = audioread('audio.wav');

                N = length(audio);

                ventana = hann(N);

                Sxx = pwelch(audio, ventana, 0, N, Fs);

                f = linspace(0, Fs/2, floor(N/2)+1);

                figure;

                plot(
                    f,
                    10*log10(Sxx(1:floor(N/2)+1))
                );

                xlabel('Frecuencia (Hz)');
                ylabel('Densidad espectral de potencia (dB/Hz)');
                title('Espectro de frecuencia del audio');

                grid on;

            catch
                disp('Error al graficar el espectro.');
            end_try_catch


        case 5

            disp('Saliendo del programa...');


        otherwise

            disp('Opcion no valida.');

    endswitch

endwhile


