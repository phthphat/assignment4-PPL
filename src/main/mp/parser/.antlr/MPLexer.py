# Generated from /home/phthphat/Documents/PPL/assignment4/Assignment4/upload/src/main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0242\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\6\r\u00d7\n\r\r\r\16\r\u00d8\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\7\16\u00e2\n\16\f\16\16\16\u00e5\13\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\7\17\u00ee\n\17\f\17\16\17")
        buf.write("\u00f1\13\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u00fb\n\20\f\20\16\20\u00fe\13\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\6 \u012f\n \r \16 \u0130\3!\6!\u0134\n!\r!\16!\u0135")
        buf.write("\3!\3!\6!\u013a\n!\r!\16!\u013b\3!\5!\u013f\n!\5!\u0141")
        buf.write("\n!\3!\5!\u0144\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\5\60\u01a4\n\60\3\60\6\60\u01a7\n\60\r\60\16\60\u01a8")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\38\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3?\3?\7?\u01f6\n?\f?\16?\u01f9\13?\3@\3@\3@\3")
        buf.write("@\7@\u01ff\n@\f@\16@\u0202\13@\3@\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3")
        buf.write("U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3")
        buf.write("]\3^\3^\5\u00e3\u00ef\u00fc\2_\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a")
        buf.write("\61c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}?\177@\u0081")
        buf.write("A\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d")
        buf.write("\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab")
        buf.write("\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5\2\u00b7B\u00b9")
        buf.write("C\u00bbD\3\2#\5\2\13\f\17\17\"\"\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\5\2C\\aac|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\6\2")
        buf.write("\n\f\16\17$$^^\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2HHh")
        buf.write("h\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\2\u0236\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\3\u00bd")
        buf.write("\3\2\2\2\5\u00bf\3\2\2\2\7\u00c1\3\2\2\2\t\u00c3\3\2\2")
        buf.write("\2\13\u00c5\3\2\2\2\r\u00c7\3\2\2\2\17\u00c9\3\2\2\2\21")
        buf.write("\u00cb\3\2\2\2\23\u00cd\3\2\2\2\25\u00cf\3\2\2\2\27\u00d2")
        buf.write("\3\2\2\2\31\u00d6\3\2\2\2\33\u00dc\3\2\2\2\35\u00eb\3")
        buf.write("\2\2\2\37\u00f6\3\2\2\2!\u0103\3\2\2\2#\u0105\3\2\2\2")
        buf.write("%\u0107\3\2\2\2\'\u0109\3\2\2\2)\u010b\3\2\2\2+\u010f")
        buf.write("\3\2\2\2-\u0113\3\2\2\2/\u0117\3\2\2\2\61\u011a\3\2\2")
        buf.write("\2\63\u011e\3\2\2\2\65\u0120\3\2\2\2\67\u0123\3\2\2\2")
        buf.write("9\u0125\3\2\2\2;\u0128\3\2\2\2=\u012a\3\2\2\2?\u012e\3")
        buf.write("\2\2\2A\u0133\3\2\2\2C\u0145\3\2\2\2E\u014d\3\2\2\2G\u0155")
        buf.write("\3\2\2\2I\u015a\3\2\2\2K\u0162\3\2\2\2M\u016a\3\2\2\2")
        buf.write("O\u0171\3\2\2\2Q\u0176\3\2\2\2S\u017a\3\2\2\2U\u0180\3")
        buf.write("\2\2\2W\u0183\3\2\2\2Y\u018c\3\2\2\2[\u0196\3\2\2\2]\u019b")
        buf.write("\3\2\2\2_\u01a1\3\2\2\2a\u01aa\3\2\2\2c\u01ad\3\2\2\2")
        buf.write("e\u01b2\3\2\2\2g\u01b7\3\2\2\2i\u01bd\3\2\2\2k\u01c0\3")
        buf.write("\2\2\2m\u01c4\3\2\2\2o\u01c7\3\2\2\2q\u01ce\3\2\2\2s\u01d4")
        buf.write("\3\2\2\2u\u01dd\3\2\2\2w\u01e4\3\2\2\2y\u01e9\3\2\2\2")
        buf.write("{\u01ef\3\2\2\2}\u01f3\3\2\2\2\177\u01fa\3\2\2\2\u0081")
        buf.write("\u0206\3\2\2\2\u0083\u0208\3\2\2\2\u0085\u020a\3\2\2\2")
        buf.write("\u0087\u020c\3\2\2\2\u0089\u020e\3\2\2\2\u008b\u0210\3")
        buf.write("\2\2\2\u008d\u0212\3\2\2\2\u008f\u0214\3\2\2\2\u0091\u0216")
        buf.write("\3\2\2\2\u0093\u0218\3\2\2\2\u0095\u021a\3\2\2\2\u0097")
        buf.write("\u021c\3\2\2\2\u0099\u021e\3\2\2\2\u009b\u0220\3\2\2\2")
        buf.write("\u009d\u0222\3\2\2\2\u009f\u0224\3\2\2\2\u00a1\u0226\3")
        buf.write("\2\2\2\u00a3\u0228\3\2\2\2\u00a5\u022a\3\2\2\2\u00a7\u022c")
        buf.write("\3\2\2\2\u00a9\u022e\3\2\2\2\u00ab\u0230\3\2\2\2\u00ad")
        buf.write("\u0232\3\2\2\2\u00af\u0234\3\2\2\2\u00b1\u0236\3\2\2\2")
        buf.write("\u00b3\u0238\3\2\2\2\u00b5\u023a\3\2\2\2\u00b7\u023c\3")
        buf.write("\2\2\2\u00b9\u023e\3\2\2\2\u00bb\u0240\3\2\2\2\u00bd\u00be")
        buf.write("\7*\2\2\u00be\4\3\2\2\2\u00bf\u00c0\7+\2\2\u00c0\6\3\2")
        buf.write("\2\2\u00c1\u00c2\7}\2\2\u00c2\b\3\2\2\2\u00c3\u00c4\7")
        buf.write("\177\2\2\u00c4\n\3\2\2\2\u00c5\u00c6\7=\2\2\u00c6\f\3")
        buf.write("\2\2\2\u00c7\u00c8\7.\2\2\u00c8\16\3\2\2\2\u00c9\u00ca")
        buf.write("\7]\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7_\2\2\u00cc\22\3")
        buf.write("\2\2\2\u00cd\u00ce\7<\2\2\u00ce\24\3\2\2\2\u00cf\u00d0")
        buf.write("\7\60\2\2\u00d0\u00d1\7\60\2\2\u00d1\26\3\2\2\2\u00d2")
        buf.write("\u00d3\7<\2\2\u00d3\u00d4\7?\2\2\u00d4\30\3\2\2\2\u00d5")
        buf.write("\u00d7\t\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\u00db\b\r\2\2\u00db\32\3\2\2\2\u00dc\u00dd")
        buf.write("\7*\2\2\u00dd\u00de\7,\2\2\u00de\u00e3\3\2\2\2\u00df\u00e2")
        buf.write("\5\33\16\2\u00e0\u00e2\13\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e3\3")
        buf.write("\2\2\2\u00e6\u00e7\7,\2\2\u00e7\u00e8\7+\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00ea\b\16\2\2\u00ea\34\3\2\2\2\u00eb\u00ef")
        buf.write("\5\7\4\2\u00ec\u00ee\13\2\2\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\5")
        buf.write("\t\5\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\b\17\2\2\u00f5")
        buf.write("\36\3\2\2\2\u00f6\u00f7\7\61\2\2\u00f7\u00f8\7\61\2\2")
        buf.write("\u00f8\u00fc\3\2\2\2\u00f9\u00fb\13\2\2\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00ff\u0100\7\f\2\2\u0100\u0101\3\2\2\2\u0101\u0102\b")
        buf.write("\20\2\2\u0102 \3\2\2\2\u0103\u0104\7-\2\2\u0104\"\3\2")
        buf.write("\2\2\u0105\u0106\7/\2\2\u0106$\3\2\2\2\u0107\u0108\7,")
        buf.write("\2\2\u0108&\3\2\2\2\u0109\u010a\7\61\2\2\u010a(\3\2\2")
        buf.write("\2\u010b\u010c\5\u0089E\2\u010c\u010d\5\u0093J\2\u010d")
        buf.write("\u010e\5\u00adW\2\u010e*\3\2\2\2\u010f\u0110\5\u009bN")
        buf.write("\2\u0110\u0111\5\u009fP\2\u0111\u0112\5\u0089E\2\u0112")
        buf.write(",\3\2\2\2\u0113\u0114\5\u009dO\2\u0114\u0115\5\u009fP")
        buf.write("\2\u0115\u0116\5\u00a9U\2\u0116.\3\2\2\2\u0117\u0118\5")
        buf.write("\u009fP\2\u0118\u0119\5\u00a5S\2\u0119\60\3\2\2\2\u011a")
        buf.write("\u011b\5\u0083B\2\u011b\u011c\5\u009dO\2\u011c\u011d\5")
        buf.write("\u0089E\2\u011d\62\3\2\2\2\u011e\u011f\7?\2\2\u011f\64")
        buf.write("\3\2\2\2\u0120\u0121\7>\2\2\u0121\u0122\7@\2\2\u0122\66")
        buf.write("\3\2\2\2\u0123\u0124\7>\2\2\u01248\3\2\2\2\u0125\u0126")
        buf.write("\7>\2\2\u0126\u0127\7?\2\2\u0127:\3\2\2\2\u0128\u0129")
        buf.write("\7@\2\2\u0129<\3\2\2\2\u012a\u012b\7@\2\2\u012b\u012c")
        buf.write("\7?\2\2\u012c>\3\2\2\2\u012d\u012f\t\3\2\2\u012e\u012d")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131@\3\2\2\2\u0132\u0134\4\62;\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u0143\3\2\2\2\u0137\u0139\7")
        buf.write("\60\2\2\u0138\u013a\4\62;\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013e\3\2\2\2\u013d\u013f\5_\60\2\u013e\u013d\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u0137")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0144\3\2\2\2\u0142")
        buf.write("\u0144\5_\60\2\u0143\u0140\3\2\2\2\u0143\u0142\3\2\2\2")
        buf.write("\u0144B\3\2\2\2\u0145\u0146\5\u00a1Q\2\u0146\u0147\5\u00a5")
        buf.write("S\2\u0147\u0148\5\u009fP\2\u0148\u0149\5\u008fH\2\u0149")
        buf.write("\u014a\5\u00a5S\2\u014a\u014b\5\u0083B\2\u014b\u014c\5")
        buf.write("\u009bN\2\u014cD\3\2\2\2\u014d\u014e\5\u0093J\2\u014e")
        buf.write("\u014f\5\u009dO\2\u014f\u0150\5\u00a9U\2\u0150\u0151\5")
        buf.write("\u008bF\2\u0151\u0152\5\u008fH\2\u0152\u0153\5\u008bF")
        buf.write("\2\u0153\u0154\5\u00a5S\2\u0154F\3\2\2\2\u0155\u0156\5")
        buf.write("\u00a5S\2\u0156\u0157\5\u008bF\2\u0157\u0158\5\u0083B")
        buf.write("\2\u0158\u0159\5\u0099M\2\u0159H\3\2\2\2\u015a\u015b\5")
        buf.write("\u0085C\2\u015b\u015c\5\u009fP\2\u015c\u015d\5\u009fP")
        buf.write("\2\u015d\u015e\5\u0099M\2\u015e\u015f\5\u008bF\2\u015f")
        buf.write("\u0160\5\u0083B\2\u0160\u0161\5\u009dO\2\u0161J\3\2\2")
        buf.write("\2\u0162\u0163\5\u0085C\2\u0163\u0164\5\u009fP\2\u0164")
        buf.write("\u0165\5\u009fP\2\u0165\u0166\5\u0099M\2\u0166\u0167\5")
        buf.write("\u008bF\2\u0167\u0168\5\u0083B\2\u0168\u0169\5\u009dO")
        buf.write("\2\u0169L\3\2\2\2\u016a\u016b\5\u00a7T\2\u016b\u016c\5")
        buf.write("\u00a9U\2\u016c\u016d\5\u00a5S\2\u016d\u016e\5\u0093J")
        buf.write("\2\u016e\u016f\5\u009dO\2\u016f\u0170\5\u008fH\2\u0170")
        buf.write("N\3\2\2\2\u0171\u0172\5\u00adW\2\u0172\u0173\5\u009fP")
        buf.write("\2\u0173\u0174\5\u0093J\2\u0174\u0175\5\u0089E\2\u0175")
        buf.write("P\3\2\2\2\u0176\u0177\5\u00adW\2\u0177\u0178\5\u0083B")
        buf.write("\2\u0178\u0179\5\u00a5S\2\u0179R\3\2\2\2\u017a\u017b\5")
        buf.write("\u0083B\2\u017b\u017c\5\u00a5S\2\u017c\u017d\5\u00a5S")
        buf.write("\2\u017d\u017e\5\u0083B\2\u017e\u017f\5\u00b3Z\2\u017f")
        buf.write("T\3\2\2\2\u0180\u0181\5\u009fP\2\u0181\u0182\5\u008dG")
        buf.write("\2\u0182V\3\2\2\2\u0183\u0184\5\u008dG\2\u0184\u0185\5")
        buf.write("\u00abV\2\u0185\u0186\5\u009dO\2\u0186\u0187\5\u0087D")
        buf.write("\2\u0187\u0188\5\u00a9U\2\u0188\u0189\5\u0093J\2\u0189")
        buf.write("\u018a\5\u009fP\2\u018a\u018b\5\u009dO\2\u018bX\3\2\2")
        buf.write("\2\u018c\u018d\5\u00a1Q\2\u018d\u018e\5\u00a5S\2\u018e")
        buf.write("\u018f\5\u009fP\2\u018f\u0190\5\u0087D\2\u0190\u0191\5")
        buf.write("\u008bF\2\u0191\u0192\5\u0089E\2\u0192\u0193\5\u00abV")
        buf.write("\2\u0193\u0194\5\u00a5S\2\u0194\u0195\5\u008bF\2\u0195")
        buf.write("Z\3\2\2\2\u0196\u0197\5\u00a9U\2\u0197\u0198\5\u00a5S")
        buf.write("\2\u0198\u0199\5\u00abV\2\u0199\u019a\5\u008bF\2\u019a")
        buf.write("\\\3\2\2\2\u019b\u019c\5\u008dG\2\u019c\u019d\5\u0083")
        buf.write("B\2\u019d\u019e\5\u0099M\2\u019e\u019f\5\u00a7T\2\u019f")
        buf.write("\u01a0\5\u008bF\2\u01a0^\3\2\2\2\u01a1\u01a3\t\4\2\2\u01a2")
        buf.write("\u01a4\t\5\2\2\u01a3\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a6\3\2\2\2\u01a5\u01a7\4\62;\2\u01a6\u01a5\3")
        buf.write("\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9`\3\2\2\2\u01aa\u01ab\5\u0093J\2\u01ab\u01ac")
        buf.write("\5\u008dG\2\u01acb\3\2\2\2\u01ad\u01ae\5\u00a9U\2\u01ae")
        buf.write("\u01af\5\u0091I\2\u01af\u01b0\5\u008bF\2\u01b0\u01b1\5")
        buf.write("\u009dO\2\u01b1d\3\2\2\2\u01b2\u01b3\5\u008bF\2\u01b3")
        buf.write("\u01b4\5\u0099M\2\u01b4\u01b5\5\u00a7T\2\u01b5\u01b6\5")
        buf.write("\u008bF\2\u01b6f\3\2\2\2\u01b7\u01b8\5\u00afX\2\u01b8")
        buf.write("\u01b9\5\u0091I\2\u01b9\u01ba\5\u0093J\2\u01ba\u01bb\5")
        buf.write("\u0099M\2\u01bb\u01bc\5\u008bF\2\u01bch\3\2\2\2\u01bd")
        buf.write("\u01be\5\u0089E\2\u01be\u01bf\5\u009fP\2\u01bfj\3\2\2")
        buf.write("\2\u01c0\u01c1\5\u008dG\2\u01c1\u01c2\5\u009fP\2\u01c2")
        buf.write("\u01c3\5\u00a5S\2\u01c3l\3\2\2\2\u01c4\u01c5\5\u00a9U")
        buf.write("\2\u01c5\u01c6\5\u009fP\2\u01c6n\3\2\2\2\u01c7\u01c8\5")
        buf.write("\u0089E\2\u01c8\u01c9\5\u009fP\2\u01c9\u01ca\5\u00afX")
        buf.write("\2\u01ca\u01cb\5\u009dO\2\u01cb\u01cc\5\u00a9U\2\u01cc")
        buf.write("\u01cd\5\u009fP\2\u01cdp\3\2\2\2\u01ce\u01cf\5\u0085C")
        buf.write("\2\u01cf\u01d0\5\u00a5S\2\u01d0\u01d1\5\u008bF\2\u01d1")
        buf.write("\u01d2\5\u0083B\2\u01d2\u01d3\5\u0097L\2\u01d3r\3\2\2")
        buf.write("\2\u01d4\u01d5\5\u0087D\2\u01d5\u01d6\5\u009fP\2\u01d6")
        buf.write("\u01d7\5\u009dO\2\u01d7\u01d8\5\u00a9U\2\u01d8\u01d9\5")
        buf.write("\u0093J\2\u01d9\u01da\5\u009dO\2\u01da\u01db\5\u00abV")
        buf.write("\2\u01db\u01dc\5\u008bF\2\u01dct\3\2\2\2\u01dd\u01de\5")
        buf.write("\u00a5S\2\u01de\u01df\5\u008bF\2\u01df\u01e0\5\u00a9U")
        buf.write("\2\u01e0\u01e1\5\u00abV\2\u01e1\u01e2\5\u00a5S\2\u01e2")
        buf.write("\u01e3\5\u009dO\2\u01e3v\3\2\2\2\u01e4\u01e5\5\u00afX")
        buf.write("\2\u01e5\u01e6\5\u0093J\2\u01e6\u01e7\5\u00a9U\2\u01e7")
        buf.write("\u01e8\5\u0091I\2\u01e8x\3\2\2\2\u01e9\u01ea\5\u0085C")
        buf.write("\2\u01ea\u01eb\5\u008bF\2\u01eb\u01ec\5\u008fH\2\u01ec")
        buf.write("\u01ed\5\u0093J\2\u01ed\u01ee\5\u009dO\2\u01eez\3\2\2")
        buf.write("\2\u01ef\u01f0\5\u008bF\2\u01f0\u01f1\5\u009dO\2\u01f1")
        buf.write("\u01f2\5\u0089E\2\u01f2|\3\2\2\2\u01f3\u01f7\t\6\2\2\u01f4")
        buf.write("\u01f6\t\7\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2")
        buf.write("\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8~\3\2\2")
        buf.write("\2\u01f9\u01f7\3\2\2\2\u01fa\u0200\5\u0081A\2\u01fb\u01fc")
        buf.write("\7^\2\2\u01fc\u01ff\t\b\2\2\u01fd\u01ff\n\t\2\2\u01fe")
        buf.write("\u01fb\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2")
        buf.write("\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0203\3")
        buf.write("\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\5\u0081A\2\u0204")
        buf.write("\u0205\b@\3\2\u0205\u0080\3\2\2\2\u0206\u0207\7$\2\2\u0207")
        buf.write("\u0082\3\2\2\2\u0208\u0209\t\n\2\2\u0209\u0084\3\2\2\2")
        buf.write("\u020a\u020b\t\13\2\2\u020b\u0086\3\2\2\2\u020c\u020d")
        buf.write("\t\f\2\2\u020d\u0088\3\2\2\2\u020e\u020f\t\r\2\2\u020f")
        buf.write("\u008a\3\2\2\2\u0210\u0211\t\4\2\2\u0211\u008c\3\2\2\2")
        buf.write("\u0212\u0213\t\16\2\2\u0213\u008e\3\2\2\2\u0214\u0215")
        buf.write("\t\17\2\2\u0215\u0090\3\2\2\2\u0216\u0217\t\20\2\2\u0217")
        buf.write("\u0092\3\2\2\2\u0218\u0219\t\21\2\2\u0219\u0094\3\2\2")
        buf.write("\2\u021a\u021b\t\22\2\2\u021b\u0096\3\2\2\2\u021c\u021d")
        buf.write("\t\23\2\2\u021d\u0098\3\2\2\2\u021e\u021f\t\24\2\2\u021f")
        buf.write("\u009a\3\2\2\2\u0220\u0221\t\25\2\2\u0221\u009c\3\2\2")
        buf.write("\2\u0222\u0223\t\26\2\2\u0223\u009e\3\2\2\2\u0224\u0225")
        buf.write("\t\27\2\2\u0225\u00a0\3\2\2\2\u0226\u0227\t\30\2\2\u0227")
        buf.write("\u00a2\3\2\2\2\u0228\u0229\t\31\2\2\u0229\u00a4\3\2\2")
        buf.write("\2\u022a\u022b\t\32\2\2\u022b\u00a6\3\2\2\2\u022c\u022d")
        buf.write("\t\33\2\2\u022d\u00a8\3\2\2\2\u022e\u022f\t\34\2\2\u022f")
        buf.write("\u00aa\3\2\2\2\u0230\u0231\t\35\2\2\u0231\u00ac\3\2\2")
        buf.write("\2\u0232\u0233\t\36\2\2\u0233\u00ae\3\2\2\2\u0234\u0235")
        buf.write("\t\37\2\2\u0235\u00b0\3\2\2\2\u0236\u0237\t \2\2\u0237")
        buf.write("\u00b2\3\2\2\2\u0238\u0239\t!\2\2\u0239\u00b4\3\2\2\2")
        buf.write("\u023a\u023b\t\"\2\2\u023b\u00b6\3\2\2\2\u023c\u023d\13")
        buf.write("\2\2\2\u023d\u00b8\3\2\2\2\u023e\u023f\13\2\2\2\u023f")
        buf.write("\u00ba\3\2\2\2\u0240\u0241\13\2\2\2\u0241\u00bc\3\2\2")
        buf.write("\2\23\2\u00d8\u00e1\u00e3\u00ef\u00fc\u0130\u0135\u013b")
        buf.write("\u013e\u0140\u0143\u01a3\u01a8\u01f7\u01fe\u0200\4\b\2")
        buf.write("\2\3@\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    LP = 3
    RP = 4
    SEMI = 5
    COMMA = 6
    LS = 7
    RS = 8
    COLON = 9
    DOUBLEDOT = 10
    ASSIGN = 11
    WS = 12
    TRADITIONALBLOCKCOMMENT = 13
    BLOCKCOMMENT = 14
    LINECOMMENT = 15
    ADD = 16
    SUB = 17
    MUL = 18
    DIVISION = 19
    DIV = 20
    MOD = 21
    NOT = 22
    OR = 23
    AND = 24
    EQUAL = 25
    NOTEQUAL = 26
    LESS = 27
    LESSEQUAL = 28
    GREATER = 29
    GREATEREQUAL = 30
    INTLIT = 31
    FLOATLIT = 32
    PROGRAM = 33
    INTTYPE = 34
    REALTYPE = 35
    BOOLTYPE = 36
    BOOLEAN = 37
    STRINGTYPE = 38
    VOIDTYPE = 39
    VAR = 40
    ARRAY = 41
    OF = 42
    FUNCTION = 43
    PROCEDURE = 44
    TRUE = 45
    FALSE = 46
    IF = 47
    THEN = 48
    ELSE = 49
    WHILE = 50
    DO = 51
    FOR = 52
    TO = 53
    DOWNTO = 54
    BREAK = 55
    CONTINUE = 56
    RETURN = 57
    WITH = 58
    BEGIN = 59
    END = 60
    ID = 61
    STRINGLIT = 62
    DQ = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "','", "'['", "']'", "':'", 
            "'..'", "':='", "'+'", "'-'", "'*'", "'/'", "'='", "'<>'", "'<'", 
            "'<='", "'>'", "'>='", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LP", "RP", "SEMI", "COMMA", "LS", "RS", "COLON", 
            "DOUBLEDOT", "ASSIGN", "WS", "TRADITIONALBLOCKCOMMENT", "BLOCKCOMMENT", 
            "LINECOMMENT", "ADD", "SUB", "MUL", "DIVISION", "DIV", "MOD", 
            "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", 
            "GREATER", "GREATEREQUAL", "INTLIT", "FLOATLIT", "PROGRAM", 
            "INTTYPE", "REALTYPE", "BOOLTYPE", "BOOLEAN", "STRINGTYPE", 
            "VOIDTYPE", "VAR", "ARRAY", "OF", "FUNCTION", "PROCEDURE", "TRUE", 
            "FALSE", "IF", "THEN", "ELSE", "WHILE", "DO", "FOR", "TO", "DOWNTO", 
            "BREAK", "CONTINUE", "RETURN", "WITH", "BEGIN", "END", "ID", 
            "STRINGLIT", "DQ", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LB", "RB", "LP", "RP", "SEMI", "COMMA", "LS", "RS", "COLON", 
                  "DOUBLEDOT", "ASSIGN", "WS", "TRADITIONALBLOCKCOMMENT", 
                  "BLOCKCOMMENT", "LINECOMMENT", "ADD", "SUB", "MUL", "DIVISION", 
                  "DIV", "MOD", "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", 
                  "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", "INTLIT", 
                  "FLOATLIT", "PROGRAM", "INTTYPE", "REALTYPE", "BOOLTYPE", 
                  "BOOLEAN", "STRINGTYPE", "VOIDTYPE", "VAR", "ARRAY", "OF", 
                  "FUNCTION", "PROCEDURE", "TRUE", "FALSE", "EXPONENT", 
                  "IF", "THEN", "ELSE", "WHILE", "DO", "FOR", "TO", "DOWNTO", 
                  "BREAK", "CONTINUE", "RETURN", "WITH", "BEGIN", "END", 
                  "ID", "STRINGLIT", "DQ", "A", "B", "C", "D", "E", "F", 
                  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('"','');
     


