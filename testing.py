import unittest
from core_logic import Estimation, Board
import server
from flask import request

class FlaskrTestCase(unittest.TestCase):
    
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()
    
    # def test_info(self):
    #     result = self.app.get('/api/v1/info')
    #     self.assertEqual(result.data, b'This is api gives access to the task management application')

    def tes_get_boards_list(self):
        result = self.app.get('/api/v1/board/list')
        print(result)
        self.assertEqual(result.data, b'qwe' )
        
        


# class TestEstimation(unittest.TestCase):

#     def setUp(self):
#         self.widget = Estimation(5, 'h')


#     def test_math_num(self):
#         self.assertEqual(self.widget.num, 5)
    
#     def test_math_pars(self):
#         self.assertEqual(self.widget.pars(), '5h')

#     def test_math_pars_day(self):
#         widget = Estimation(20, 'h')
#         self.assertEqual(widget.pars(), '2d4h')

#     def test_math_creat_day(self):
#         widget = Estimation(5, 'd')
#         self.assertEqual(widget.num, 40)

#     def test_math_creat_pars_day(self):
#         widget = Estimation(5, 'd')
#         self.assertEqual(widget.pars(), '1w')

#     def test_math_creat_week(self):
#         widget = Estimation(5, 'w')
#         self.assertEqual(widget.num, 200)

#     def test_math_creat_pars_week(self):
#         widget = Estimation(5, 'w')
#         self.assertEqual(widget.pars(), '1m1w')

#     def test_math_creat_month(self):
#         widget = Estimation(5, 'm')
#         self.assertEqual(widget.num, 800)

#     def test_math_creat_pars_month(self):
#         widget = Estimation(5, 'm')
#         self.assertEqual(widget.pars(), '5m')
    

#     def test_add_is_obj(self):
#         widget1 = Estimation(2, 'h')
#         widget2 = Estimation(2, 'h')
#         widget3 = widget1 + widget2
#         self.assertIsInstance(widget3, Estimation)

#     def test_add_h(self):
#         widget1 = Estimation(2, 'h')
#         widget2 = Estimation(2, 'h')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '4h')
    
#     def test_add_d(self):
#         widget1 = Estimation(7, 'h')
#         widget2 = Estimation(1, 'h')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '1d')

#     def test_add_d_h(self):
#         widget1 = Estimation(9, 'h')
#         widget2 = Estimation(1, 'h')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '1d2h')
    
#     def test_add_d_d(self):
#         widget1 = Estimation(4, 'd')
#         widget2 = Estimation(1, 'd')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '1w')
    
#     def test_add_w_d(self):
#         widget1 = Estimation(2, 'w')
#         widget2 = Estimation(2, 'd')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '2w2d')
    
#     def test_add_w_w(self):
#         widget1 = Estimation(4, 'w')
#         widget2 = Estimation(1, 'w')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '1m1w')
    
#     def test_add_m_d(self):
#         widget1 = Estimation(2, 'm')
#         widget2 = Estimation(5, 'd')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '2m1w')

#     def test_add_interesting(self):
#         widget1 = Estimation(256, 'h')
#         widget2 = Estimation(16, 'd')
#         widget3 = widget1 + widget2
#         self.assertEqual(widget3.pars(), '2m1w3d')
    

# # class TestBoard(unittest.TestCase):
# #     def setUp(self):
# #         self.widget = Board('Bob', 'Доска разработчика', ['ToDo', 'InProgress', 'Done'])

# #     def test_atr_pars(self):
# #         self.assertAlmostEqual(self.widget.columns, 'ToDo,InProgress,Done')
    
# #     def test_create_from_dict(self):

# #         data = {
# #                 "title": "Доска разработчика",
# #                 "columns": [
# #                              "ToDo",
# #                              "InProgress",
# #                              "Done"
# #                 ] }
# #         self.assertIsInstance(self.widget.create_from_dict(data), self.widget)

if __name__ == '__main__':
    unittest.main()