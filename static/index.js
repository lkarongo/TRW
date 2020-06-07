var map, places;
        var markers = [];
        var autocomplete;
        var staterestrict = {'state': 'california'};

            var states = {
                'california': {
                    center: {lat: 36.7783, lng: -119.4179},
                    zoom: 6
                },
                'nevada': {
                    center: {lat: 38.8026, lng: -116.4194},
                    zoom: 7
                }
            };

    function initMap() {
            map = new google.maps.Map(document.getElementById('map'), {
                zoom: states['california'].zoom,
                center: states['california'].center,
                mapTypeControl: false,
                panControl: false,
                zoomControl: false,
                streetViewControl: false
            });

            function auto() {
                autocomplete = new google.maps.places.Autocomplete((document.getElementById('txtplaces')),{
                    types: ['address']
            });
                places = new google.maps.places.PlacesService(map);
                autocomplete.addListener('place_changed', onPlaceChanged);
            }

    }

            function onPlaceChanged() {
            var place = autocomplete.getPlace();
            if (place.geometry) {
                map.panTo(place.geometry.location);
                map.setZoom(15)
                search();
            } else {
                document.getElementById('txtplaces').placeholder = 'Street Address, City, Zip Code';
            }
        }

        google.maps.event.addDomListener(window, 'load', initMap, onPlaceChanged);




