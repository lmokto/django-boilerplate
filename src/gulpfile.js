'use strict';

// Load npm modules
var gulp = require('gulp');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');

// Sass
gulp.task('style:sass', function() {
  return gulp.src(['static/src/styles/main.scss'])
    .pipe(sourcemaps.init())
      .pipe(sass({ outputStyle: 'compressed' }))
      .pipe(concat('main.min.css'))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('static/dist/css/'));
});

// Javascript
gulp.task('scripts:js', function() {
  return gulp.src(['static/src/js/**/*.js'])
    .pipe(sourcemaps.init())
      .pipe(concat('main.min.js'))
      .pipe(uglify())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('static/dist/js/'));
});

// Watches
gulp.task('watch', function() {
  gulp.watch('static/src/styles/**/*.*', ['style:sass']);
  gulp.watch('static/src/js/**/*.js', ['scripts:js']);
});

// Default
gulp.task('default', ['style:sass', 'scripts:js', 'watch']);

