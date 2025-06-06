from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from libgen_api import LibgenSearch

class BookSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({'error': 'Missing query param ?q='}, status=status.HTTP_400_BAD_REQUEST)

        s = LibgenSearch()
        raw_results = s.search_title(query)
        results = []

        for book in raw_results[:10]:  # Limit to first 10 results
            title = book.get('Title')
            author = book.get('Author')
            publisher = book.get('Publisher')
            year = book.get('Year')
            language = book.get('Language')
            extension = book.get('Extension')
            mirrors = {
                "Mirror_1": book.get('Mirror_1'),
                "Mirror_2": book.get('Mirror_2'),
                "Mirror_3": book.get('Mirror_3'),
            }

            # Build response with placeholders where needed
            results.append({
                "title": title,
                "series": None,  # Placeholder, not available from LibGen
                "author": author,
                "rating": 4.5,  # Placeholder static rating
                "votes": 1200,  # Placeholder static vote count
                "reading_status": "Want to read",
                "user_rating": None,  # Can be added later
                "annotation": "No description available. Can be added later.",
                "price": "$1.99",  # Placeholder price
                "preview_link": mirrors["Mirror_1"],  # Just using Mirror_1 as preview
                "age_limit": "16+",
                "copyright_holder": publisher,
                "publisher": publisher,
                "narrator": "Unknown",  # Not available from LibGen
                "tags": ["Fantasy", "Adventure", "Fiction"],  # Sample tags
                "file_format": extension,
                "language": language,
                "year": year,
                "download_links": mirrors,
            })

        return Response(results)