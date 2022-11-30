from tree import Tree

class TestStack:
    '''Class Stack in Stack.py'''

    def test_get_element_by_id(self):
  # <body>
  #   <div id="main">
  #     <h1 id="heading">Title</h1>
  #     <h2>Subtitle</h2>
  #   </div>
  # </body>

        '''get_element_by_id test'''
    tree = Tree(
      {
        'tag_name': 'body',
        'id': None,
        'children': [
          {
            'tag_name': 'div',
            'id': 'main',
            'children': [
              {
                'tag_name': 'h1',
                'id': 'heading',
                'text_content': 'Title',
                'children': []
              },
              {
                'tag_name': 'h2',
                'id': None,
                'text_content': 'Subitle',
                'children': []
              }
            ]
          }
        ]
      }
    )
    assert(tree.get_element_by_id('heading') =={
      'tag_name': 'h1',
      'id': 'heading',
      'text_content': 'Title',
      'children': []
    } )

    assert(tree.get_element_by_id('nope') == None)
