
module.exports = function (app, router) {
  app.use('/api', require('./home.js')(router));
  // app.use('/api/users',require('./user_end'));
};