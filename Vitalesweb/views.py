from django.shortcuts import render, redirect


def index_view(request):
    """Vista principal (Home) con carousel, clientes, estadísticas y CTA"""
    context = {
        'carousel_slides': [
            {
                'image': 'images/hero_atencion_medica_1764968445128.png',
                'title': 'Atención Médica a Domicilio',
                'description': 'Servicios de salud integral con calidad y calidez humana',
                'active': True
            },
            {
                'image': 'images/hero_ambulancia_1764968457921.png',
                'title': 'Traslados en Ambulancia',
                'description': 'Transporte médico seguro y profesional las 24 horas',
                'active': False
            },
            {
                'image': 'images/hero_cuidados_especializados_1764968471136.png',
                'title': 'Cuidados Especializados',
                'description': 'Equipo multidisciplinario comprometido con tu bienestar',
                'active': False
            }
        ],
        'statistics': [
            {
                'icon': 'bi-people-fill',
                'number': '20000',
                'label': 'Pacientes Atendidos',
                'prefix': '+ de '
            },
            {
                'icon': 'bi-truck-front-fill',
                'number': '6500',
                'label': 'Traslados Nacionales',
                'prefix': '+ de '
            },
            {
                'icon': 'bi-house-heart-fill',
                'number': '1800',
                'label': 'Hospitalizaciones en Casa',
                'prefix': '+ de '
            }
        ],
        'clients': [
            {'name': 'PDVSA', 'logo': 'img/pdvsa_logo.png', 'logo_class': ''},
            {'name': 'Venemergencia', 'logo': 'img/venemergencia_logo.png', 'logo_class': 'logo-small'},
            {'name': 'Bancamiga', 'logo': 'img/bancamiga_logo.png', 'logo_class': 'logo-small'},
            {'name': 'Bolivariana de Puertos', 'logo': 'img/bolivariana_puertos_logo.png', 'logo_class': ''},
            {'name': 'La Mundial de Seguros', 'logo': 'img/lamundial_logo.jpg', 'logo_class': ''},
            {'name': 'UCNE', 'logo': 'img/ucne_logo.png', 'logo_class': ''},
        ],
        'instagram_url': 'https://www.instagram.com/vitales.vzla/'
    }
    return render(request, 'Vitalesweb/index.html', context)


def nosotros_view(request):
    """Vista Nosotros con misión, visión y valores"""
    context = {
        'mission': 'Proveer servicios de salud integral a domicilio con calidad, accesibilidad y '
                   'calidez humana, satisfaciendo las necesidades de cada paciente.',
        'vision': 'Ser la empresa líder en la transformación y consolidación de la atención a '
                  'domicilio, reconocida por la excelencia y el compromiso de nuestro equipo '
                  'multidisciplinario.',
        'values': [
            {
                'name': 'Confianza',
                'icon': 'bi-heart-pulse-fill',
                'description': 'Relaciones basadas en la credibilidad y el respeto mutuo',
                'bg_color': 'bg-info',
                'text_color': 'text-info'
            },
            {
                'name': 'Innovación',
                'icon': 'bi-lightbulb',
                'description': 'Mejora continua en nuestros servicios y procesos',
                'bg_color': 'bg-info',
                'text_color': 'text-info'
            },
            {
                'name': 'Compromiso',
                'icon': 'bi-star-fill',
                'description': 'Dedicación total con nuestro propósito y pacientes',
                'bg_color': 'bg-danger',
                'text_color': 'text-danger'
            },
            {
                'name': 'Excelencia',
                'icon': 'bi-award',
                'description': 'Calidad superior en cada atención que brindamos',
                'bg_color': 'bg-success',
                'text_color': 'text-success'
            },
        ],
        'team_image': 'images/equipo_vitales_profesional_1765720906420.png'
    }
    return render(request, 'Vitalesweb/nosotros.html', context)


def servicios_view(request):
    """Vista Servicios con todos los servicios ofrecidos"""
    context = {
        'services': [
            {
                'title': 'Atención Médica a Domicilio',
                'icon': 'bi-house-heart',
                'description': 'Consultas médicas profesionales en la comodidad de tu hogar con equipos especializados.',
                'image': 'images/servicio_atencion_domicilio_1764968502963.png'
            },
            {
                'title': 'Traslados en Ambulancia',
                'icon': 'bi-truck-front',
                'description': 'Servicio de transporte médico equipado y disponible las 24 horas del día.',
                'image': 'images/servicio_ambulancia_1764968516060.png'
            },
            {
                'title': 'Cuidados de Enfermería',
                'icon': 'bi-heart-pulse-fill',
                'description': 'Personal de enfermería calificado para cuidados continuos y especializados.',
                'image': 'images/servicio_enfermeria_1764968528056.png'
            },
            {
                'title': 'Terapia Respiratoria',
                'icon': 'bi-lungs',
                'description': 'Tratamientos respiratorios personalizados con equipos de última generación.',
                'image': 'images/servicio_terapia_respiratoria_1764968543539.png'
            },
            {
                'title': 'Laboratorio',
                'icon': 'bi-droplet-fill',
                'description': 'Toma de muestras y análisis clínicos a domicilio con resultados confiables.',
                'image': 'images/servicio_laboratorio_1764968557037.png'
            },
            {
                'title': 'RX, EKG y Ecos',
                'icon': 'bi-activity',
                'description': 'Estudios diagnósticos cardiovasculares y radiológicos en tu hogar.',
                'image': 'images/servicio_diagnosticos_1764968569824.png'
            },
            {
                'title': 'Sueroterapia',
                'icon': 'bi-droplet-half',
                'description': 'Hidratación y administración intravenosa de medicamentos de forma segura.',
                'image': 'images/servicio_sueroterapia_1764968587467.png'
            },
            {
                'title': 'Fisioterapia',
                'icon': 'bi-person-arms-up',
                'description': 'Rehabilitación física personalizada para recuperación y bienestar.',
                'image': 'images/servicio_fisioterapia_1764968599655.png'
            },
            {
                'title': 'Alquiler de Concentradores de Oxígeno',
                'icon': 'bi-wind',
                'description': 'Equipos de oxigenoterapia de alta calidad disponibles para alquiler.',
                'image': 'images/servicio_oxigeno_1764968612828.png'
            },
            {
                'title': 'Administración de Tratamientos VEV',
                'icon': 'bi-capsule',
                'description': 'Tratamientos endovenosos administrados por personal especializado.',
                'image': 'images/servicio_tratamientos_vev_1764968626103.png'
            },
            {
                'title': 'Cobertura de Salud Corporativa y Eventos',
                'icon': 'bi-building',
                'description': 'Servicios médicos integrales para empresas y eventos especiales.',
                'image': 'images/servicio_corporativo_1764968638340.png'
            },
        ]
    }
    return render(request, 'Vitalesweb/servicios.html', context)


def contacto_redirect(request):
    """Redirección a Instagram de Vitales"""
    return redirect('https://www.instagram.com/vitales.vzla/')
