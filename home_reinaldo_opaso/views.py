from django.shortcuts import render, Http404

# ==============================================================================
# DATOS DE GÉNEROS Y PELÍCULAS (DATASET EN MEMORIA)
# ==============================================================================

DATA_GENEROS = [
    {
        'id': 'accion',
        'nombre': 'Acción y Aventura',
        'descripcion': 'Películas llenas de dinamismo, persecuciones intensas, combates y adrenalina sin descanso.',
        'icono': 'bi-fire',
        'color_badge': 'danger',
        'total_titulos': 10
    },
    {
        'id': 'ciencia_ficcion',
        'nombre': 'Ciencia Ficción y Espacio',
        'descripcion': 'Exploraciones espaciales, futuros distópicos, inteligencia artificial y fenómenos cuánticos.',
        'icono': 'bi-rocket-takeoff-fill',
        'color_badge': 'info',
        'total_titulos': 10
    }
]

DATA_PELICULAS = {
    'accion': [
        {
            'id': 1,
            'titulo': 'Mad Max: Fury Road',
            'anio': 2015,
            'director': 'George Miller',
            'duracion': '120 min',
            'calificacion': 8.1,
            'imagen': 'img/mad_max.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'En un desierto postapocalíptico, Max se une a Furiosa para escapar del tirano Immortan Joe.',
            'destacada': True
        },
        {
            'id': 2,
            'titulo': 'John Wick 4',
            'anio': 2023,
            'director': 'Chad Stahelski',
            'duracion': '169 min',
            'calificacion': 7.7,
            'imagen': 'img/john_wick.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'John Wick descubre un camino para derrotar a la Alta Mesa, enfrentándose a nuevos y letales enemigos.',
            'destacada': True
        },
        {
            'id': 3,
            'titulo': 'The Dark Knight',
            'anio': 2008,
            'director': 'Christopher Nolan',
            'duracion': '152 min',
            'calificacion': 9.0,
            'imagen': 'img/dark_knight.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Batman se enfrenta a su mayor prueba psicológica y física cuando el Joker desata el caos en Gotham.',
            'destacada': True
        },
        {
            'id': 4,
            'titulo': 'Gladiator',
            'anio': 2000,
            'director': 'Ridley Scott',
            'duracion': '155 min',
            'calificacion': 8.5,
            'imagen': 'img/gladiator.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un general romano traicionado busca venganza contra el corrupto emperador que asesinó a su familia.',
            'destacada': False
        },
        {
            'id': 5,
            'titulo': 'Top Gun: Maverick',
            'anio': 2022,
            'director': 'Joseph Kosinski',
            'duracion': '130 min',
            'calificacion': 8.3,
            'imagen': 'img/top_gun.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1519074069444-1ba4ea16e6e2?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Maverick regresa para entrenar a una nueva generación de pilotos para una misión especializada y peligrosa.',
            'destacada': True
        },
        {
            'id': 6,
            'titulo': 'Mission: Impossible - Fallout',
            'anio': 2018,
            'director': 'Christopher McQuarrie',
            'duracion': '147 min',
            'calificacion': 7.7,
            'imagen': 'img/mission_impossible.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Ethan Hunt y su equipo corren contra el tiempo tras una misión fallida para recuperar plutonio robado.',
            'destacada': False
        },
        {
            'id': 7,
            'titulo': 'The Matrix',
            'anio': 1999,
            'director': 'Lana & Lilly Wachowski',
            'duracion': '136 min',
            'calificacion': 8.7,
            'imagen': 'img/matrix.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un hacker informático aprende sobre la verdadera naturaleza de su realidad y su rol en la guerra.',
            'destacada': True
        },
        {
            'id': 8,
            'titulo': 'Die Hard',
            'anio': 1988,
            'director': 'John McTiernan',
            'duracion': '132 min',
            'calificacion': 8.2,
            'imagen': 'img/die_hard.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un policía de Nueva York intenta salvar a su esposa y a otros rehenes capturados en un rascacielos.',
            'destacada': False
        },
        {
            'id': 9,
            'titulo': 'Casino Royale',
            'anio': 2006,
            'director': 'Martin Campbell',
            'duracion': '144 min',
            'calificacion': 8.0,
            'imagen': 'img/casino_royale.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'James Bond obtiene su licencia para matar y se enfrenta al banquero privado terrorista Le Chiffre.',
            'destacada': False
        },
        {
            'id': 10,
            'titulo': 'Speed',
            'anio': 1994,
            'director': 'Jan de Bont',
            'duracion': '116 min',
            'calificacion': 7.3,
            'imagen': 'img/speed.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1508974239320-0a029497e820?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un oficial de policía debe evitar que una bomba explote a bordo de un autobús de pasajeros en movimiento.',
            'destacada': False
        }
    ],
    'ciencia_ficcion': [
        {
            'id': 11,
            'titulo': 'Interstellar',
            'anio': 2014,
            'director': 'Christopher Nolan',
            'duracion': '169 min',
            'calificacion': 8.7,
            'imagen': 'img/interstellar.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un equipo de exploradores viaja a través de un agujero de gusano en el espacio buscando un nuevo hogar para la humanidad.',
            'destacada': True
        },
        {
            'id': 12,
            'titulo': 'Blade Runner 2049',
            'anio': 2017,
            'director': 'Denis Villeneuve',
            'duracion': '164 min',
            'calificacion': 8.0,
            'imagen': 'img/blade_runner.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un joven Blade Runner desentierra un secreto oculto que lo lleva a buscar al desaparecido Rick Deckard.',
            'destacada': True
        },
        {
            'id': 13,
            'titulo': 'Dune: Part Two',
            'anio': 2024,
            'director': 'Denis Villeneuve',
            'duracion': '166 min',
            'calificacion': 8.6,
            'imagen': 'img/dune.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Paul Atreides se une a Chani y a los Fremen en una guerra de venganza contra los conspiradores de su familia.',
            'destacada': True
        },
        {
            'id': 14,
            'titulo': 'Inception',
            'anio': 2010,
            'director': 'Christopher Nolan',
            'duracion': '148 min',
            'calificacion': 8.8,
            'imagen': 'img/inception.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1507499739999-097706ad8914?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'A un ladrón que roba secretos corporativos mediante tecnología de sueños se le asigna la tarea inversa.',
            'destacada': True
        },
        {
            'id': 15,
            'titulo': 'Arrival',
            'anio': 2016,
            'director': 'Denis Villeneuve',
            'duracion': '116 min',
            'calificacion': 7.9,
            'imagen': 'img/arrival.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Una lingüista es reclutada por el ejército para comunicarse con formas de vida extraterrestres.',
            'destacada': False
        },
        {
            'id': 16,
            'titulo': '2001: A Space Odyssey',
            'anio': 1968,
            'director': 'Stanley Kubrick',
            'duracion': '149 min',
            'calificacion': 8.3,
            'imagen': 'img/2001.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1447433589675-4aaa569f3e05?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un monolito misterioso conecta la evolución humana con una travesía espacial guiada por la IA HAL 9000.',
            'destacada': False
        },
        {
            'id': 17,
            'titulo': 'The Martian',
            'anio': 2015,
            'director': 'Ridley Scott',
            'duracion': '144 min',
            'calificacion': 8.0,
            'imagen': 'img/the_martian.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un astronauta queda varado en Marte tras una tormenta y debe usar su ingenio científico para sobrevivir.',
            'destacada': False
        },
        {
            'id': 18,
            'titulo': 'Alien',
            'anio': 1979,
            'director': 'Ridley Scott',
            'duracion': '117 min',
            'calificacion': 8.5,
            'imagen': 'img/alien.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'La tripulación de una nave espacial comercial descubre una forma de vida extraterrestre letal.',
            'destacada': False
        },
        {
            'id': 19,
            'titulo': 'Terminator 2: Judgment Day',
            'anio': 1991,
            'director': 'James Cameron',
            'duracion': '137 min',
            'calificacion': 8.6,
            'imagen': 'img/terminator2.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un ciborg reprogramado es enviado para proteger al joven John Connor de un modelo de metal líquido avanzado.',
            'destacada': True
        },
        {
            'id': 20,
            'titulo': 'Ex Machina',
            'anio': 2014,
            'director': 'Alex Garland',
            'duracion': '108 min',
            'calificacion': 7.7,
            'imagen': 'img/ex_machina.jpg',
            'imagen_remota': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=600&auto=format&fit=crop&q=80',
            'sinopsis': 'Un programador participa en un experimento innovador para evaluar las cualidades humanas de una IA humanoide.',
            'destacada': False
        }
    ]
}


def vista_inicio(request):
    """
    Vista principal (raíz /).
    Muestra la bienvenida y el listado de géneros disponibles en componentes de Bootstrap.
    """
    context = {
        'titulo_seccion': 'Bienvenido a CineHub',
        'subtitulo': 'Tu plataforma de exploración cinematográfica desarrollada con Django y Bootstrap 5.',
        'generos': DATA_GENEROS,
        'total_generos': len(DATA_GENEROS),
        'estudiante': 'Reinaldo Opaso'
    }
    return render(request, 'home_app/inicio.html', context)


def vista_peliculas_genero(request, genero_id):
    """
    Vista de listado de películas por género.
    Muestra al menos 10 películas para el género seleccionado utilizando tarjetas de Bootstrap y filtros.
    """
    genero_seleccionado = None
    for g in DATA_GENEROS:
        if g['id'] == genero_id:
            genero_seleccionado = g
            break

    if not genero_seleccionado:
        raise Http404("El género solicitado no se encuentra en nuestro catálogo.")

    peliculas = DATA_PELICULAS.get(genero_id, [])

    # Filtro opcional por texto de búsqueda: ?q=palabra
    busqueda = request.GET.get('q', '').strip()
    if busqueda:
        peliculas = [p for p in peliculas if busqueda.lower() in p['titulo'].lower() or busqueda.lower() in p['director'].lower()]

    # Filtro opcional por año mínimo: ?anio=2015
    filtro_anio = request.GET.get('anio', '').strip()
    if filtro_anio and filtro_anio.isdigit():
        peliculas = [p for p in peliculas if p['anio'] >= int(filtro_anio)]

    context = {
        'genero': genero_seleccionado,
        'peliculas': peliculas,
        'total_peliculas': len(peliculas),
        'busqueda': busqueda,
        'filtro_anio': filtro_anio
    }
    return render(request, 'home_app/peliculas.html', context)


def vista_contacto(request):
    """
    Vista de formulario para sugerencias y contacto.
    Gestiona peticiones GET y POST con validación y mensaje de confirmación en pantalla.
    """
    mensaje_enviado = False
    datos_recibidos = {}

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        genero_elegido = request.POST.get('genero_elegido', '').strip()
        pelicula_sugerida = request.POST.get('pelicula_sugerida', '').strip()
        comentario = request.POST.get('comentario', '').strip()

        datos_recibidos = {
            'nombre': nombre,
            'correo': correo,
            'genero': genero_elegido,
            'pelicula': pelicula_sugerida,
            'comentario': comentario
        }
        mensaje_enviado = True

    context = {
        'mensaje_enviado': mensaje_enviado,
        'datos': datos_recibidos,
        'generos_disponibles': DATA_GENEROS
    }
    return render(request, 'home_app/contacto.html', context)
